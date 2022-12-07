from brownie import accounts, NFTToken, Contract


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    deployer = accounts.load('deployer')
    nft: Contract = NFTToken[0]
    # NFTToken.publish_source(nft)
    for i in chunks(list(range(2, 10001)), 100):
        nft.mint(i, {'from': deployer})
