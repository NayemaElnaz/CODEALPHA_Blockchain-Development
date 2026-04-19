# CODEALPHA_Blockchain-Development
Blockchain technology and decentralized application development.

## Task 1:
Simple Storage Smart Contract

This project implements a basic smart contract on the Ethereum blockchain. It allows a user to store an integer value and modify it using increment and decrement functions. 

## 🛠 Tech Stack
- Smart Contract: Solidity (v0.8.0)
- Deployment: Python (Web3.py)
- Local Blockchain: Ganache
- Tools: Terminal, Notepad
- remix

## 🚀 Key Features
- Integer Storage: Securely holds a signed integer (`int256`) on-chain.
- Increment Function: Adds 1 to the current stored value.
- Decrement Function: Subtracts 1 from the current stored value.
- Public Visibility: The value is readable by any external application.

  ### Task 1 Output:
  <img width="1177" height="433" alt="Screenshot 2026-04-17 125100" src="https://github.com/user-attachments/assets/062b7547-52ad-4a42-8905-baab31b5fbf1" />
  <img width="1364" height="624" alt="remix task1" src="https://github.com/user-attachments/assets/59f8f8da-2bdf-4a3f-8e18-abd392c661e4" />
<img width="1364" height="708" alt="task11" src="https://github.com/user-attachments/assets/fc36aa86-bd69-4a83-868f-b7f2f0a35ba4" />

---

## Task 4: 
🔒 CryptoLock Smart Contract

A time-locked "Savings Vault" smart contract. This project demonstrates how to handle **Ether transactions**, **Mappings**, and **Time-based restrictions** on the Ethereum blockchain.

## Technical Implementation
- Value Control: Uses the `payable` modifier to securely receive Ether.
- Security: Implements the "Checks-Effects-Interactions" pattern in the `withdraw` function to prevent re-entrancy.
- State Management: Tracks individual user balances and timestamps using Solidity Mappings.

## How It Works
1. Deposit: Users send Ether and specify a duration (in seconds).
2. Lock: The contract calculates `block.timestamp + duration`.
3. Validation: The `withdraw` function checks if the current time has surpassed the lock time.

## Local Development
- Compiler: Solidity 0.8.0
- Interaction: Web3.py & Python 3.x
- Network: Ganache CLI

### Task 4 Output:
<img width="1366" height="731" alt="Screenshot 2026-04-18 213314" src="https://github.com/user-attachments/assets/3b4c239b-1082-4af1-b9fa-0a4c21239489" />
<img width="1347" height="713" alt="Screenshot 2026-04-18 213214" src="https://github.com/user-attachments/assets/458725c1-5aba-447e-8757-3d2b9ad666ec" />
### Result:
<img width="1071" height="533" alt="Screenshot 2026-04-18 214913" src="https://github.com/user-attachments/assets/6c81e63b-74ff-492b-af6f-06a470da1717" />

---

# Task 2: 
Multi-Send Smart Contract

This project focuses on the efficient distribution of assets on the Ethereum blockchain. The Multi-Send contract allows a user to send Ether to multiple recipients in a single transaction, significantly reducing manual effort and ensuring data consistency.

## 🛠 Features:
- Array Processing: Accepts a dynamic list of Ethereum addresses.
- Equal Distribution Logic: Automatically calculates and sends equal shares of the sent Ether.
- Transaction Safety: Uses the `call` method with success checks to ensure all transfers are completed correctly.

## 🚀 Tech Stack
- Solidity: Smart contract logic and loops.
- Web3.py: Automated testing suite.
- Ganache: Local blockchain environment.

  ### Task 2 Output:
 <img width="883" height="382" alt="Screenshot 2026-04-19 183334" src="https://github.com/user-attachments/assets/63124457-566c-4fed-ad91-62495fbe1df0" />

 ---

 
 





































