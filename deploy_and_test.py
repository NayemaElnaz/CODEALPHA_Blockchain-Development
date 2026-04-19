from web3 import Web3
from solcx import install_solc, compile_standard

# 1. Setup
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
install_solc("0.8.0")

with open("./MultiSend.sol", "r") as file:
    source = file.read()

compiled = compile_standard({
    "language": "Solidity",
    "sources": {"MultiSend.sol": {"content": source}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode.object"]}}}
}, solc_version="0.8.0")

abi = compiled["contracts"]["MultiSend.sol"]["MultiSend"]["abi"]
bytecode = compiled["contracts"]["MultiSend.sol"]["MultiSend"]["evm"]["bytecode"]["object"]

# 2. Deploy
account = w3.eth.accounts[0]
MultiSend = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = MultiSend.constructor().transact({"from": account})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=receipt.contractAddress, abi=abi)
print(f"🚀 MultiSend Deployed at: {receipt.contractAddress}")

# 3. Task: Distribute 3 ETH to 3 different accounts
recipients = [w3.eth.accounts[1], w3.eth.accounts[2], w3.eth.accounts[3]]
amount_to_send = w3.to_wei(3, "ether")

print(f"\nDistributing {w3.from_wei(amount_to_send, 'ether')} ETH to {len(recipients)} recipients...")

tx = contract.functions.distributeEther(recipients).transact({
    "from": account, 
    "value": amount_to_send
})
w3.eth.wait_for_transaction_receipt(tx)

print("✅ Success: All recipients received their equal share!")
for i, addr in enumerate(recipients):
    balance = w3.from_wei(w3.eth.get_balance(addr), 'ether')
    print(f"Recipient {i+1} ({addr[:10]}...): {balance} ETH")