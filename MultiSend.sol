// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiSend {
    // Function to send Ether to multiple addresses equally
    function distributeEther(address[] memory _recipients) public payable {
        require(_recipients.length > 0, "Recipient list cannot be empty");
        require(msg.value > 0, "Must send some Ether to distribute");

        // Calculate equal share
        uint256 amountPerPerson = msg.value / _recipients.length;

        for (uint256 i = 0; i < _recipients.length; i++) {
            // Transfer the share to each recipient
            (bool success, ) = _recipients[i].call{value: amountPerPerson}("");
            require(success, "Transfer failed to one of the addresses");
        }
    }

    // Fallback function to allow the contract to receive plain Ether
    receive() external payable {}
}