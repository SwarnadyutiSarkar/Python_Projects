// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FoodSupplyChain {
    struct FoodItem {
        uint id;
        string name;
        string origin;
        string currentLocation;
        address owner;
        string[] history;
    }

    mapping(uint => FoodItem) public foodItems;
    uint public itemCount;

    event FoodItemCreated(uint id, string name, string origin, address owner);
    event FoodItemUpdated(uint id, string currentLocation, address owner);

    function createFoodItem(string memory _name, string memory _origin) public {
        itemCount++;
        string[] memory history;
        foodItems[itemCount] = FoodItem(itemCount, _name, _origin, _origin, msg.sender, history);
        emit FoodItemCreated(itemCount, _name, _origin, msg.sender);
    }

    function updateLocation(uint _id, string memory _newLocation) public {
        FoodItem storage item = foodItems[_id];
        require(msg.sender == item.owner, "Only the owner can update location");
        item.currentLocation = _newLocation;
        item.history.push(_newLocation);
        emit FoodItemUpdated(_id, _newLocation, msg.sender);
    }

    function getFoodItem(uint _id) public view returns (string memory, string memory, string memory, address, string[] memory) {
        FoodItem memory item = foodItems[_id];
        return (item.name, item.origin, item.currentLocation, item.owner, item.history);
    }
}
