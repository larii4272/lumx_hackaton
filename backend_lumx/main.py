import contract, project, wallet, token_
from enums import ContractType, AccountType
import time

if __name__ == "__main__":
    my_project = project.Project()
    my_project.generate_apikey(blockchain=AccountType.ETHEREUM.value)
    my_contract = contract.Contract(my_project)
    my_contract.create_contract("first_commit", "FCM", "First Commit", ContractType.NON_FUNGIBLE.value)
    my_wallet = wallet.Wallet(my_project)
    
    transaction = my_wallet.invoke_custom_transaction(my_wallet, "0x94ED59118CA26708Cef7E98D35a6f47f30ca6998", "createAuction(string , string , uint256 , uint256)", 
                                         ["https://azure-bitter-grasshopper-987.mypinata.cloud/ipfs/Qmb46mvqWRLd6SDxfyovrwgUbFJtHBFwcDzRZ5a15TkDz1", 
                                          "aloo", 1000000000000000000,2], 0)

    time.sleep(30)

    transaction.read_transaction()

    #my_contract.create_token("my_token", "First Token", 10000)
    #my_project.mint_tokens(my_contract, my_wallet, 10, my_contract.uriNumber)

    #my_project.transfer_tokens(my_contract)
    print("\n\n")
    #my_contract.read_token_type()
    

