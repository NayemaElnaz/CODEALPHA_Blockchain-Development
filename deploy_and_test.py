import time
from web3 import Web3
from solcx import install_solc, compile_standard

# 1. Setup
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
install_solc("0.8.0")

with open("./PollingSystem.sol", "r") as file:
    source = file.read()

compiled = compile_standard({
    "language": "Solidity",
    "sources": {"PollingSystem.sol": {"content": source}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode.object"]}}}
}, solc_version="0.8.0")

abi = compiled["contracts"]["PollingSystem.sol"]["PollingSystem"]["abi"]
bytecode = compiled["contracts"]["PollingSystem.sol"]["PollingSystem"]["evm"]["bytecode"]["object"]

# 2. Deploy
account = w3.eth.accounts[0]
PollingSystem = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = PollingSystem.constructor().transact({"from": account})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=receipt.contractAddress, abi=abi)
print(f"🚀 Polling System Deployed at: {receipt.contractAddress}")

# 3. Create a Poll (5 seconds duration)
print("\n--- Creating a Poll ---")
options = ["Option A", "Option B", "Option C"]
contract.functions.createPoll("Best Internship?", options, 5).transact({"from": account})
print("Poll created: 'Best Internship?' with 3 options.")

# 4. Cast Votes from different accounts
print("\n--- Casting Votes ---")
contract.functions.vote(0, 0).transact({"from": w3.eth.accounts[1]}) # Vote for A
contract.functions.vote(0, 0).transact({"from": w3.eth.accounts[2]}) # Vote for A
contract.functions.vote(0, 1).transact({"from": w3.eth.accounts[3]}) # Vote for B
print("Votes registered from 3 different accounts.")

# 5. Wait for poll to end and force block mining
print("\nWaiting for poll to end...")
time.sleep(7)
w3.provider.make_request("evm_mine", [])

# 6. Get Winner
winner = contract.functions.getWinner(0).call()
print(f"🏆 The Winner is: {winner[0]} with {winner[1]} votes!")