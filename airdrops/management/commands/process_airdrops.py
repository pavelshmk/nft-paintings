import json
import logging
from datetime import datetime
from time import sleep

import requests
from constance import config
from django.core.management import BaseCommand
from django.db import transaction

from airdrops.models import Airdrop


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                with transaction.atomic():
                    airdrops = requests.get(config.AIRDROP_API_PREFIX).json()
                    cnt = 0
                    for airdrop in airdrops:
                        _, added = Airdrop.objects.get_or_create(
                            id=airdrop['id'],
                            defaults={
                                'user_id': airdrop['user_id'],
                                'tokens': airdrop['tokens'],
                                'address': airdrop['bep_address'],
                                'datetime': datetime.fromisoformat(airdrop['created_date_time']),
                            }
                        )
                        if added:
                            cnt += 1
                        requests.delete('{}{}'.format(config.AIRDROP_API_PREFIX, airdrop['id']))
                    if cnt > 0:
                        logging.warning('{} airdrops added'.format(cnt))
            except KeyboardInterrupt:
                return
            except Exception as e:
                logging.exception(e)
            sleep(5)
