# import solcx
from solcx import compile_standard, install_solc

# import json
import json

# import Web3
from web3 import Web3

# import os
import os

# import environment
from dotenv import load_dotenv

load_dotenv()
# it automatically looks for .env file and imports it into our script


# using simplestorage in python
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)

# compile solidity
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)


# print compiled_sol
# print(compiled_sol)

# output and print the compiled to a new file
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# for deploying and testing the code we need the bitecode and abi
# for the etherium virtual michine (evm) to understand
# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# print(abi)

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:6755"))

# get chain_id or networkid
chain_id = 1337
# lot of error 5777 to 1337 not working
# so

# add an address fom ganache
my_address = "0xab7f92c3f0eb6b803003C437d5efB3Fb446c3EbF"

# for signing transactions we need private_key
# it is not safe to put the private_key directly in the code
# add 0x in the private_key
#
# access the private key fom environment variable
private_key = os.getenv("PRIVATE_KEY")
# private_key = os.environ.get("PRIVATE_KEY")
# print(private_key)
# print(os.environ["PRIVATE_KEY"])
# another way is creating a .env file
# .env to .gitignore so wedont accidently push it to github
# print(os.getenv("BOOM"))

# create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)

# get latest transaction
nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)
# we wil get 0 because there is no transaction done yet

# need to build sign and send transaction

# SimpleStorage dosent have a construcror
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": w3.eth.chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
# print(transaction)
# signing the tranction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print(signed_txn)
# send this transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# wait for block conformation
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# working with contract : you need
# contract address
# contract abi
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
