import requests
import json

#@TODO TALVEZ CRIAR UMA CLASSE TOKEN? 
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
        print(f"Contract created with success! {response.text}")
        response_dict = json.loads(response.text)
        self.contractId = response_dict["id"]
        self.contractAddress = response_dict["address"]
    
    def create_token(self, name, description, maxSupply, imageUrl):
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
        #print(response.text)
        response_dict = json.loads(response.text)
        self.tokenTypeId = response_dict["id"]
        self.uriNumber = response_dict["uriNumber"]
        self.tokens.append(response_dict) #@TODO criar uma classe pro token?
   
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

