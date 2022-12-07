// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.3;

import "OpenZeppelin/openzeppelin-contracts@4.1.0/contracts/token/ERC721/ERC721.sol";
import "OpenZeppelin/openzeppelin-contracts@4.1.0/contracts/access/Ownable.sol";

contract NFTToken is Ownable, ERC721 {
    uint256 public totalSupply;
    uint256 public constant MAX_SUPPLY = 10000;
    string public baseURI;

    constructor(string memory baseURI_) ERC721("SafeBull", "SAFEBULL") {
        baseURI = baseURI_;
    }

    function updateBaseURI(string memory baseURI_) public {
        baseURI = baseURI_;
    }

    function mint(uint256[] calldata tokenIds) public onlyOwner {
        require(totalSupply + tokenIds.length <= MAX_SUPPLY, "resulting amount exceeds MAX_SUPPLY");
        for (uint256 i = 0; i < tokenIds.length; i++) {
            _mint(msg.sender, tokenIds[i]);
        }
        totalSupply += tokenIds.length;
    }

    function _baseURI() internal virtual override view returns (string memory) {
        return baseURI;
    }
}
