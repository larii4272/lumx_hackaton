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
        #print(response.text)
        response_dict = json.loads(response.text) #str -> dict
        self.apiKey = response_dict['apiKey']

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
        url = "https://protocol-sandbox.lumx.io/v2/contracts/{contractId}"
        headers = {"Authorization": f"Bearer {self.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def read_all_contracts(self):
        url = "https://protocol-sandbox.lumx.io/v2/contracts"
        headers = {"Authorization": "Bearer <token>"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def mint_tokens(self, contract, wallet, quantity, uriNumber):
        url = "https://protocol-sandbox.lumx.io/v2/transactions/mints"
        payload = {
            "contractId": f"{contract.contractId}",
            "walletId": f"{contract.walletId}",
            "quantity": quantity,
            "uriNumber": uriNumber
        }
        headers = {
            "Authorization": f"Bearer {self.apiToken}",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        response_dict = json.loads(response.text)
        self.tokenId = response_dict["id"]

