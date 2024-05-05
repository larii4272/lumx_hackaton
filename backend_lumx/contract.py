import requests
import json
from backend_lumx import token_

class Contract():

    def __init__(self, project): 
        self.project = project
        self.tokens = [] # Como ele explicou na live, é por ordem numérica. Da pra usar o index da lista
        
    def create_contract(self, name, symbol, description, type_):
        # Creating a contract
        url = "https://protocol-sandbox.lumx.io/v2/contracts"

        payload = {
            "name": f"{name}",
            "symbol": f"{symbol}",
            "description": f"{description}",
            "type": f"{type_}"
        }
        headers = {
            "Authorization": f"Bearer {self.project.apiKey}",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(f"\nContract created with success! {response.text}")
        response_dict = json.loads(response.text)
        self.contractId = response_dict["id"]
        self.contractAddress = response_dict["address"]
        self.project.my_contracts.append(self)

    def create_token(self, name, description, maxSupply, imageUrl=None):
        url = f"https://protocol-sandbox.lumx.io/v2/contracts/{self.contractId}/token-types"
        payload = {
            "name": f"{name}",
            "description": f"{description}",
            "maxSupply": maxSupply,
            "traits": {},
            "imageUrl": f"{imageUrl}"
        }
        headers = {
            "Authorization": f"Bearer {self.project.apiKey}",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(f"creating token on create token function {response.text}")
        response_dict = json.loads(response.text)

        tokenTypeName = response_dict["name"]
        uriNumber = response_dict["uriNumber"]
        new_token = token_.Token_(self,uriNumber, tokenTypeName)
        self.tokens.append(new_token) 
   
    #***********************READ METHODS***********************:
    def read_token_type(self):
        url = f"https://protocol-sandbox.lumx.io/v2/contracts/{self.contractId}/token-types/{self.uriNumber}"
        headers = {"Authorization": f"Bearer {self.project.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def read_all_token_types(self):
        url = f"https://protocol-sandbox.lumx.io/v2/contracts/{self.contractId}/token-types"
        headers = {"Authorization": f"Bearer {self.project.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)
    
    def read_contract(self, contract):
        url = f"https://protocol-sandbox.lumx.io/v2/contracts/{contract.contractId}"
        headers = {"Authorization": f"Bearer {self.apiKey}"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)

