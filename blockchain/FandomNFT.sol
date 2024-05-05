// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/*   _________    _   ______  ____  __  ___   _   ______________
   / ____/   |  / | / / __ \/ __ \/  |/  /  / | / / ____/_  __/
  / /_  / /| | /  |/ / / / / / / / /|_/ /  /  |/ / /_    / /   
 / __/ / ___ |/ /|  / /_/ / /_/ / /  / /  / /|  / __/   / /    
/_/   /_/  |_/_/ |_/_____/\____/_/  /_/  /_/ |_/_/     /_/                                                                 
*/
contract FandomNFT is ERC721URIStorage {

    //removido onlyOwner e outras validacoes
    // para nao ter problemas para o Hackaton

    using Strings for uint256;

    uint256 public totalSupply;
    uint256 public constant PERCENTAGE_DIVISOR = 100;
    uint256 public constant OWNER_FEE_PERCENTAGE = 5;

    struct Token {
        uint256 tokenId;
        string name;
        uint256 initValue;
        string metadata;
        bool available;
        uint256 dateCheckIn;
    }
    mapping(uint256 => Token) public tokensCreated;

    event callCreateToken(uint256 indexed tokenId);
    event TokenPurchased(address indexed buyer, uint256 indexed tokenId, uint256 amount);
    event Paused(address account);
    event Unpaused(address account);
    event Withdraw(address to, uint256 amount);

    address public owner;
    bool public paused;

    constructor() ERC721("FandomNFT", "FAN") {
        owner = msg.sender;
        paused = false;
    }

    function getOwner() external view returns (address) {
        return owner;
    }

    function pause() external {
        paused = true;
        emit Paused(msg.sender);
    }

    function unpause() external {
        paused = false;
        emit Unpaused(msg.sender);
    }

    function withdraw(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner).transfer(amount);
        emit Withdraw(owner, amount);
    }

    function createToken(
        string memory metadata,
        string memory name,
        uint256 initValue
    ) external {
        require(!paused, "Contract is paused");

        uint256 newTokenId = totalSupply;

        string memory tokenURI = string(
            abi.encodePacked(
                "https://azure-bitter-grasshopper-987.mypinata.cloud/ipfs/",
                metadata
            )
        );

        tokensCreated[newTokenId] = Token(
            newTokenId,
            name,
            initValue,
            tokenURI,
            true,
            0
        );

        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        totalSupply++;
        emit callCreateToken(newTokenId);
    }

    function purchaseToken(uint256 tokenId) external payable {
        require(!paused, "Contract is paused");
        require(tokensCreated[tokenId].available, "Token not available");

        // Calculate contract Fee
        uint256 contractFee = (msg.value * OWNER_FEE_PERCENTAGE) / PERCENTAGE_DIVISOR;
        uint256 ownerFee = msg.value - contractFee;

        payable(ownerOf(tokenId)).transfer(ownerFee);

        // Transfer token to buyer
        _transfer(ownerOf(tokenId), msg.sender, tokenId);

        tokensCreated[tokenId].dateCheckIn = block.timestamp;
        tokensCreated[tokenId].initValue = msg.value;

        emit TokenPurchased(msg.sender, tokenId, msg.value);
    }
}
