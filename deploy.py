# import solcx
from solcx import compile_standard

# using simplestorage in python
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

# compile solidity
compiled_sol = compile_standard(
    "language": "Solidity",
    "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
    
)