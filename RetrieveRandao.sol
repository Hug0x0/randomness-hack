pragma solidity >=0.8.18;

contract RandomNumberGenerator {
    mapping(uint256 => uint256) public _randomNumbers;
    uint public blockNumber;
    bytes32 public blockHashNow;
    bytes32 public blockHashPrevious;
    mapping(address => uint256) public blockNumbersToBeUsed;

    function getRandomNumber() public returns (uint256) {
        uint256 blockNumberToBeUsed = blockNumbersToBeUsed[msg.sender];
        uint256 randomNumber = block.prevrandao(blockNumberToBeUsed);

        return block.prevrandao;
    }

    function storeRandomNumber(uint256 key) public {
        _randomNumbers[key] = getRandomNumber();
    }

    function getBlockHashInfo() public returns (bytes32) {
        blockNumber = block.number;
        blockHashNow = blockhash(blockNumber);
        blockHashPrevious = blockhash(blockNumber - 1);
    }

    function getBlockHashTimestamp() public view returns (uint256) {
        return block.timestamp;
    }

    function getRandomNumbersMap(uint256 key) public view returns (uint256) {
        return _randomNumbers[key];
    }
}
