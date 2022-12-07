from brownie import accounts, NFTToken, Contract


def main():
    deployer = accounts.load('paintings-deployer')
    nft: Contract = NFTToken.deploy('http://5.63.158.203/meta/', {'from': deployer})
    NFTToken.publish_source(nft)
