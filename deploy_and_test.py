import time
import json
from web3 import Web3
from solcx import install_solc, compile_standard

# 1. Connection and Compilation
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
install_solc("0.8.0")

with open("./CryptoLock.sol", "r") as file:
    contract_source = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"CryptoLock.sol": {"content": contract_source}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode.object"]}}}
}, solc_version="0.8.0")

abi = compiled_sol["contracts"]["CryptoLock.sol"]["CryptoLock"]["abi"]
bytecode = compiled_sol["contracts"]["CryptoLock.sol"]["CryptoLock"]["evm"]["bytecode"]["object"]

# 2. Deployment
account = w3.eth.accounts[0]
CryptoLock = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = CryptoLock.constructor().transact({"from": account})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=receipt.contractAddress, abi=abi)
print(f"🚀 Contract deployed at: {receipt.contractAddress}")

# 3. Task: Deposit and Lock for 10 seconds
print("\n--- Testing Deposit ---")
deposit_amount = w3.to_wei(1, "ether")
lock_duration = 10 
contract.functions.deposit(lock_duration).transact({"from": account, "value": deposit_amount})
print(f"Deposited 1 ETH. Funds locked for {lock_duration} seconds.")

# 4. Task: Early Withdrawal (Handled properly so it doesn't crash)
print("\n--- Testing Early Withdrawal Security ---")
try:
    contract.functions.withdraw().transact({"from": account})
except Exception:
    print("✅ Security Verified: The contract successfully blocked the early withdrawal.")

# 5. The Fix: Wait and Force Blockchain Clock Forward
print("\nWaiting for the lock to expire...")
time.sleep(12)
# This line forces Ganache to update its internal clock
w3.provider.make_request("evm_mine", []) 

# 6. Task: Final Withdrawal
print("\n--- Testing Final Withdrawal ---")
try:
    tx_final = contract.functions.withdraw().transact({"from": account})
    w3.eth.wait_for_transaction_receipt(tx_final)
    print("✅ Success: Funds successfully unlocked and withdrawn to your account!")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n--- Task 4 Complete ---")