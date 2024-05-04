import requests
import json

class User():

    def __init__(self, project):
        self.project = project #By the project, we are able to pull all contracts and wallets
        pass

    def mint_tokens(self):
        url = "https://protocol-sandbox.lumx.io/v2/transactions/mints"
        payload = {
            "contractId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "walletId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "quantity": 123,
            "uriNumber": 123
        }
        headers = {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)


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


    def invoke_custom_transaction(self, wallet, contract, functionSignature, argumentsValues):
        url = "https://protocol-sandbox.lumx.io/v2/transactions/custom"

        payload = {
            "walletId": f"{wallet.walletId}",
            "contractAddress": f"{contract.contractAddress}",
            "operations": [
                {
                    "functionSignature": f"{functionSignature}",
                    "argumentsValues": [f"{argumentsValues}"],
                    "messageValue": 123
                }
            ]
        }
        headers = {
            "Authorization": f"Bearer {self.project.apiKey}",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)


