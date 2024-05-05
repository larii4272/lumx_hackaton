from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

from backend_lumx import project, contract, wallet


#Create automatically a table of Login and Password
class CustomUser(AbstractUser): 
    #username = models.CharField(max_length=50)   
    #password = models.CharField(max_length=20)   
    project = project.Project()
    project.generate_apikey()
    apiKey = models.CharField(max_length=1500, default=project.apiKey)  
    print("ABove api_key") 
    print(project.apiKey)

class Wallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    walletAddress = models.CharField(max_length=100, blank=True)  # Campo para salvar o endereço da carteira
    walletId = models.CharField(max_length=100, blank=True)       # Campo para salvar o ID da carteira

    def save(self, *args, **kwargs):
        # Antes de salvar, obtenha o projeto associado ao usuário
        project_instance = self.user.project   
        print("Below api_key")  
        print(self.user.project.apiKey)
        # Use o projeto para criar a carteira
        wallet_instance = wallet.Wallet(project_instance) 
        self.walletAddress = wallet_instance.walletAddress
        self.walletId = wallet_instance.walletId
        super().save(*args, **kwargs)  # Salva a instância do modelo OpenWallet no banco de dados



    