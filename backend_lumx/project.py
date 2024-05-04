import requests
import json
class Project():

    def __init__(self):
        self.my_wallets = []
        self.my_contracts = []  


    def generate_apikey(self):
        url = "https://protocol-sandbox.lumx.io/v2/projects/auth"
        payload = {
            "name": "first_commit",
            "blockchainName": "Chiliz"
        }
        headers = {"Content-Type": "application/json"}

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        response_dict = json.loads(response.text) #str -> dict
        self.apiKey = response_dict['apiKey']
        self.createdAt = response_dict['createdAt']

    #***********************CONTRACT METHODS***********************:

    def deploy_contract(self, contract):
        url = f"https://protocol-sandbox.lumx.io/v2/contracts/{contract.contractId}/deploy"
        headers = {"Authorization": f"Bearer {self.apiToken}"}
        response = requests.request("POST", url, headers=headers)
        print(response.text)

    def update_contract(self, contract, name, symbol, description):
        url = f"https://protocol-sandbox.lumx.io/v2/contracts/{contract.contractId}"

        payload = {
            "name": f"{name}",
            "symbol": f"{symbol}",
            "description": f"{description}",
        }
        headers = {
            "Authorization": f"Bearer {self.apiToken}",
            "Content-Type": "application/json"
        }

        response = requests.request("PATCH", url, json=payload, headers=headers)

        print(response.text)


    #***********************TRANSACTION METHODS***********************:
    def mint_tokens(self, contract, wallet, quantity, uriNumber):
        url = "https://protocol-sandbox.lumx.io/v2/transactions/mints"
        payload = {
            "contractId": f"{contract.contractId}",
            "walletId": f"{wallet.walletId}",
            "quantity": quantity,
            "uriNumber": uriNumber
        }
        headers = {
            "Authorization": f"Bearer {self.apiKey}",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        response_dict = json.loads(response.text)

        print(f"minting token on mint token function {response_dict}")
        self.logId = response_dict["logId"]

    def transfer_tokens(self, contract, from_, to_, token):
        url = "https://protocol-sandbox.lumx.io/v2/transactions/transfers"

        payload = {
            "contractId": f"{contract.contractId}",
            "from": f"{from_}",
            "to": f"{to_}",
            "tokenId": f"{token}"
        }
        headers = {
            "Authorization": f"Bearer {self.project.apiKey}",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)

    def invoke_custom_transaction(self, wallet, contract, functionSignature, argumentsValues, messageValue):
        url = "https://protocol-sandbox.lumx.io/v2/transactions/custom"

        payload = {
            "walletId": f"{wallet.walletId}",
            "contractAddress": f"{contract.contractAddress}",
            "operations": [
                {
                    "functionSignature": f"{functionSignature}",
                    "argumentsValues": [f"{argumentsValues}"],
                    "messageValue": messageValue
                }
            ]
        }
        headers = {
            "Authorization": f"Bearer {self.project.apiKey}",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)

    #***********************READ METHODS***********************:
    def read_wallet(self, wallet):
        url = f"https://protocol-sandbox.lumx.io/v2/wallets/{wallet.walletId}"
        headers = {"Authorization": f"Bearer {self.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def read_all_wallets(self):
        url = "https://protocol-sandbox.lumx.io/v2/wallets"
        headers = {"Authorization": f"Bearer {self.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def read_contract(self, contract):
        url = f"https://protocol-sandbox.lumx.io/v2/contracts/{contract.contractId}"
        headers = {"Authorization": f"Bearer {self.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def read_all_contracts(self):
        url = "https://protocol-sandbox.lumx.io/v2/contracts"
        headers = {"Authorization": "Bearer <token>"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def read_transaction(self, transactionId):
        url = f"https://protocol-sandbox.lumx.io/v2/transactions/{transactionId}"
        headers = {"Authorization": f"Bearer {self.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def read_all_transactions(self):
        url = "https://protocol-sandbox.lumx.io/v2/transactions"
        headers = {"Authorization": f"Bearer {self.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

