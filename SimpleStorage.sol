// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    // 1. Declare an integer variable (public makes it readable)
    int256 public value;

    // 2. Increment function
    function increment() public {
        value = value + 1;
    }

    // 3. Decrement function
    function decrement() public {
        value = value - 1;
    }
}