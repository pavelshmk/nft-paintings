import json
import logging

from admin_actions.admin import ActionsModelAdmin
from constance import config
from django.conf import settings
from django.contrib import admin, messages
from django.shortcuts import redirect
from web3 import Web3, HTTPProvider

from airdrops.models import Airdrop


with open(settings.BASE_DIR / 'nft_paintings' / 'erc20.abi.json') as f:
    TOKEN_ABI = json.load(f)


def process_airdrop(request, airdrops):
    w3 = Web3(HTTPProvider(config.AIRDROP_ETHEREUM_RPC))
    nonce = w3.eth.getTransactionCount(config.AIRDROP_ADDRESS)
    for airdrop in airdrops:
        if airdrop.processed:
            messages.error(request, '#{} This airdrop is already processed'.format(airdrop.pk))
            return

        try:
            token = w3.eth.contract(address=config.AIRDROP_TOKEN, abi=TOKEN_ABI)
            decimals = 10 ** token.functions.decimals().call()
            gas_price = w3.eth.gasPrice

            address = w3.toChecksumAddress(airdrop.address)
            if not token.functions.balanceOf(address).call():
                messages.error(request, '#{} Address does not own any tokens'.format(airdrop.pk))
                return

            tx = token.functions.transfer(address, int(airdrop.tokens * decimals)).buildTransaction({
                'from': config.AIRDROP_ADDRESS,
                'gasPrice': gas_price,
                'nonce': nonce,
            })
            signed = w3.eth.account.sign_transaction(tx, config.AIRDROP_PK)
            txid = w3.eth.send_raw_transaction(signed.rawTransaction)
            nonce += 1
            airdrop.processed = True
            airdrop.txid = txid.hex()
            airdrop.save(update_fields=('processed', 'txid'))
            messages.success(request, '#{} Transaction sent, txid: {}'.format(airdrop.pk, txid.hex()))
        except Exception as e:
            logging.exception(e)
            messages.error(request, '#{} An error has occurred: {}. See logs for more info'.format(airdrop.pk, e))


@admin.register(Airdrop)
class AirdropAdmin(ActionsModelAdmin):
    list_display = 'id', 'user_id', 'address', 'tokens', 'datetime', 'processed',
    actions_row = actions_detail = 'process',
    date_hierarchy = 'datetime'
    actions = 'process_batch',

    @admin.action(description='Process selected airdrops')
    def process_batch(self, request, queryset):
        process_airdrop(request, queryset)

    def process(self, request, pk):
        airdrop = Airdrop.objects.get(pk=pk)
        process_airdrop(request, [airdrop])
        return redirect('admin:airdrops_airdrop_changelist')
    process.short_description = 'Process'

