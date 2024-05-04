import contract, project, wallet
from enums import ContractType


if __name__ == "__main__":
    my_project = project.Project()
    my_project.generate_apikey()
    my_contract = contract.Contract(my_project)
    my_contract.create_contract("first_commit", "FCM", "First Commit", ContractType.NON_FUNGIBLE.value)
    my_wallet = wallet.Wallet(my_project)
    my_wallet.create_wallet()

