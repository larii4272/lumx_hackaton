import contract, project, wallet
from enums import ContractType


if __name__ == "__main__":
    my_project = project.Project()
    my_project.generate_apikey()
    my_contract = contract.Contract(my_project)
    my_contract.create_contract("first_commit", "FCM", "First Commit", ContractType.NON_FUNGIBLE.value)
    my_wallet = wallet.Wallet(my_project)
    my_wallet.create_wallet()

    my_contract.create_token("my_token", "First Token", 10000)
    my_project.mint_tokens(my_contract, my_wallet, 10, my_contract.uriNumber)

    #my_project.transfer_tokens(my_contract)
    print("\n\n")
    my_contract.read_token_type()
    

