from eth_account import Account

from web3 import Web3

def createNewETHWallet():
    count=0
    while True:
        count=count+1
        account = Account.create()
        privateKey = account._key_obj
        publicKey = privateKey.public_key 
        address = publicKey.to_checksum_address()
        if address[len(address)-6:len(address)]=="888888":
            print("privateKey:", privateKey)
            print("publicKey:", publicKey)
            print("address:", address)
            print("count:",count)
            break
    return privateKey, publicKey, address



createNewETHWallet()