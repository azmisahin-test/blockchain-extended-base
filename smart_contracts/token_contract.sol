// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Token {
    string public name = "Custom Token";
    string public symbol = "CTK";
    uint8 public decimals = 18;
    uint public totalSupply = 1000000 * (10 ** uint(decimals));

    mapping(address => uint) balances;

    constructor() {
        balances[msg.sender] = totalSupply;
    }

    function balanceOf(address owner) public view returns (uint) {
        return balances[owner];
    }

    function transfer(address to, uint value) public returns (bool) {
        require(balances[msg.sender] >= value, "Insufficient balance.");
        balances[msg.sender] -= value;
        balances[to] += value;
        return true;
    }
}
