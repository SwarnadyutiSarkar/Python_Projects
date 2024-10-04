// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DigitalWill {
    struct Will {
        uint id;
        address owner;
        string content; // This could be a URL or IPFS hash pointing to the actual document
        bool isActive;
    }

    mapping(uint => Will) public wills;
    uint public willCount;

    event WillCreated(uint id, address owner, string content);
    event WillUpdated(uint id, string content);
    event WillRevoked(uint id);

    function createWill(string memory _content) public {
        willCount++;
        wills[willCount] = Will(willCount, msg.sender, _content, true);
        emit WillCreated(willCount, msg.sender, _content);
    }

    function updateWill(uint _id, string memory _newContent) public {
        Will storage will = wills[_id];
        require(msg.sender == will.owner, "Only the owner can update the will");
        require(will.isActive, "Will is not active");
        will.content = _newContent;
        emit WillUpdated(_id, _newContent);
    }

    function revokeWill(uint _id) public {
        Will storage will = wills[_id];
        require(msg.sender == will.owner, "Only the owner can revoke the will");
        require(will.isActive, "Will is already revoked");
        will.isActive = false;
        emit WillRevoked(_id);
    }

    function getWill(uint _id) public view returns (address, string memory, bool) {
        Will memory will = wills[_id];
        return (will.owner, will.content, will.isActive);
    }
}
