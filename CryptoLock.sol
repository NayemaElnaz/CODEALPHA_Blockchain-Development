// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CryptoLock {
    // Mapping to store how much Ether each address has deposited
    mapping(address => uint256) public balances;
    // Mapping to store the exact timestamp when funds become unlockable
    mapping(address => uint256) public lockTime;

    // The 'payable' keyword allows this function to receive Ether
    function deposit(uint256 _secondsToLock) public payable {
        require(msg.value > 0, "You must deposit some Ether");
        
        balances[msg.sender] += msg.value;
        // block.timestamp is the current time in seconds
        lockTime[msg.sender] = block.timestamp + _secondsToLock;
    }

    function withdraw() public {
        // Check if the current time is greater than the stored lock time
        require(block.timestamp >= lockTime[msg.sender], "Funds are still locked!");
        require(balances[msg.sender] > 0, "No funds to withdraw.");

        uint256 amount = balances[msg.sender];
        
        // Safety First: Reset balance to 0 BEFORE sending money to prevent re-entrancy
        balances[msg.sender] = 0;
        
        // Send the Ether back to the user
        payable(msg.sender).transfer(amount);
    }

    // Helper function to check how much time is left
    function getSecondsRemaining() public view returns (uint256) {
        if (block.timestamp >= lockTime[msg.sender]) {
            return 0;
        } else {
            return lockTime[msg.sender] - block.timestamp;
        }
    }
}