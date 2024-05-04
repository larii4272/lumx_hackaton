from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

from backend_lumx import project, contract, wallet
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

#Create automatically a table of Login and Password
class CustomUser(AbstractUser): 
    project = project.Project()
    project.generate_apikey()
    apiKey = models.CharField(max_length=1000, default=project.apiKey)
    def __str__(self):
        return self.name

class OpenWallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        # Antes de salvar, obtenha o projeto associado ao usuário
        project_instance = self.user.project    
        # Use o projeto para criar a carteira
        self.wallet = wallet.Wallet(project_instance) 
        super(OpenWallet, self).save(*args, **kwargs)
        print("Uepa, essa é minha self.wallet")
        print(self.wallet)

class CreateContract(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        # Antes de salvar, obtenha o projeto associado ao usuário
        project_instance = self.user.project    
        # Use o projeto para criar a carteira
        self.contract = contract.Contract(project_instance) 
        super(CreateContract, self).save(*args, **kwargs)
    