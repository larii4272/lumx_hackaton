
import requests
import json
class Wallet():

    def __init__(self, project) -> None:
        self.project = project

    def create_wallet(self):
        url = "https://protocol-sandbox.lumx.io/v2/wallets"
        headers = {"Authorization": f"Bearer {self.project.apiKey}"}
        response = requests.request("POST", url, headers=headers)
        print(response.text)
        response_dict = json.loads(response.text)
        self.walletAddress = response_dict['address']
        self.walletId = response_dict['id']

