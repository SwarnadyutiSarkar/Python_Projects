// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ThreatIntelligence {
    struct Threat {
        string threatType;
        string description;
        string reporter;
        uint256 timestamp;
    }

    Threat[] public threats;

    event NewThreat(uint256 index, string threatType, string description, string reporter, uint256 timestamp);

    function addThreat(string memory threatType, string memory description, string memory reporter) public {
        threats.push(Threat(threatType, description, reporter, block.timestamp));
        emit NewThreat(threats.length - 1, threatType, description, reporter, block.timestamp);
    }

    function getThreats() public view returns (Threat[] memory) {
        return threats;
    }
}
