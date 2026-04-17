import json
from web3 import Web3
from solcx import install_solc, compile_standard

# 1. Connect to Ganache (Ensure Ganache is running in another terminal!)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# 2. Compile Solidity Code
print("Compiling Contract...")
install_solc("0.8.0")
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "evm.bytecode.object"]}
            }
        },
    },
    solc_version="0.8.0",
)

# 3. Get Bytecode and ABI (Fixed the Metadata error here)
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# 4. Deploy
print("Deploying contract...")
account = w3.eth.accounts[0]
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction to deploy
tx_hash = SimpleStorage.constructor().transact({"from": account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"✅ Contract successfully deployed at: {tx_receipt.contractAddress}")

# 5. Run the Internship Tasks
print(f"Initial Value: {contract.functions.value().call()}")

print("Executing Increment (+1)...")
contract.functions.increment().transact({"from": account})
print(f"Value after increment: {contract.functions.value().call()}")

print("Executing Decrement (-1)...")
contract.functions.decrement().transact({"from": account})
print(f"Value after decrement: {contract.functions.value().call()}")