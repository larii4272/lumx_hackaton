# forms.py
from django import forms
from django.db import models
from django.forms import ModelForm, TextInput, NumberInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app_lumxs.models import CustomUser, Wallet, Transaction, SolidityToken
from backend_lumx import project, non_classes
import json


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",max_length=20)
    password = forms.CharField(label='Password', max_length=40, widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

# Form to Edit Number of Pills for an Elder
class EditTokensForm(forms.Form):    
    def __init__(self, user, *args, **kwargs):
        super(EditTokensForm, self).__init__(*args, **kwargs)
        elder_pills = user.elder.medicinebox_set.all()
        for pill in elder_pills:
            self.fields[pill.pills.name] = forms.IntegerField(initial=pill.number_of_pills, min_value=0)
            
path_createtoken = "./sol_contracts/create_token.json"

#********************API Functions Communicating with Solidity****************************

# Create Token: 

class SolidityCreateToken(forms.Form):
    metadata = forms.CharField(max_length=1000)
    name = forms.CharField(max_length=100)
    tokenValue = forms.IntegerField()
    wallet = forms.ModelChoiceField(queryset=Wallet.objects.all())  # Use ModelChoiceField para selecionar um objeto Wallet
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    def save(self, *args, **kwargs):

        with open(path_createtoken, 'r') as file:
            create_token = json.load(file)

        walletInstance = self.cleaned_data['wallet']  # Obtenha a instância de Wallet do formulário
        walletIdInstance = walletInstance.walletId
        print("\nBelow api_key")  
        
        user_instance = self.cleaned_data['user']
        apiKeyInstance = user_instance.apiKey

        transactionId = non_classes.invoke_custom_transaction(create_token['outsideContractAddress'], create_token['functionSignature'],
                                              [self.cleaned_data['metadata'], self.cleaned_data['name'], self.cleaned_data['tokenValue']], create_token['messageValue'], walletIdInstance, apiKeyInstance)
        transactionName = self.cleaned_data['name']
        # Criar uma instância do modelo Transaction e salvá-la
        transaction_instance = Transaction.objects.create(transactionId=transactionId, transactionName=transactionName)
        transaction_instance.save()
        solidity_token = SolidityToken(metadata=self.cleaned_data['metadata'], name=self.cleaned_data['name'], tokenValue=self.cleaned_data['tokenValue'])
        solidity_token.save()

#@TODO
path_createtoken = "./sol_contracts/create_auction.json"
class CreateAuctionToken(forms.Form):
    metadata = forms.CharField(max_length=1000)
    name = forms.CharField(max_length=100)
    tokenValue = forms.IntegerField()
    days = forms.IntegerField()
    wallet = forms.ModelChoiceField(queryset=Wallet.objects.all())  # Use ModelChoiceField para selecionar um objeto Wallet
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    def save(self, *args, **kwargs):

        with open(path_createtoken, 'r') as file:
            create_token = json.load(file)

        walletInstance = self.cleaned_data['wallet']  # Obtenha a instância de Wallet do formulário
        walletIdInstance = walletInstance.walletId
        print("\nBelow api_key")  
        
        user_instance = self.cleaned_data['user']
        apiKeyInstance = user_instance.apiKey
        transactionId = non_classes.invoke_custom_transaction(create_token['outsideContractAddress'], create_token['functionSignature'],
                                              [self.cleaned_data['metadata'], self.cleaned_data['name'], self.cleaned_data['tokenValue'], self.cleaned_data['days']], 
                                              create_token['messageValue'], walletIdInstance, apiKeyInstance)
        transactionName = self.cleaned_data['name']
        # Criar uma instância do modelo Transaction e salvá-la
        transaction_instance = Transaction.objects.create(transactionId=transactionId, transactionName=transactionName)
        transaction_instance.save()


    