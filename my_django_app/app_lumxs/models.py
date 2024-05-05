from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

from backend_lumx import project, contract, wallet


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None,**extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, primary_key=True)
    project = project.Project()
    project.generate_apikey()
    apiKey = models.CharField(max_length=1500, default=project.apiKey)   
    print(project.apiKey)

    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username
    
    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, perm, obj=None):
        return True 
    
    def check_password(self, raw_password: str) -> bool:
        return super().check_password(raw_password)
    
class Wallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    walletAddress = models.CharField(max_length=100, blank=True)  # Campo para salvar o endereço da carteira
    walletId = models.CharField(max_length=100, blank=True)       # Campo para salvar o ID da carteira

    def save(self, *args, **kwargs):
        # Antes de salvar, obtenha o projeto associado ao usuário
        project_instance = self.user.project   
        print("\nBelow api_key")  
        print(self.user.project.apiKey)
        # Use o projeto para criar a carteira
        wallet_instance = wallet.Wallet(project_instance) 
        self.walletAddress = wallet_instance.walletAddress
        self.walletId = wallet_instance.walletId
        super().save(*args, **kwargs)  # Salva a instância do modelo OpenWallet no banco de dados

class Contract(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contractType = models.CharField(max_length=100)
    contractAddress = models.CharField(max_length=100, blank=True)  # Campo para salvar o endereço da carteira
    contractId = models.CharField(max_length=100, blank=True)       # Campo para salvar o ID da carteira

    def save(self, *args, **kwargs):
        # Antes de salvar, obtenha o projeto associado ao usuário
        project_instance = self.user.project   
        contract_instance = contract.Contract(project_instance) 
        name = self.cleaned_data['name']
        symbol = self.cleaned_data['symbol']
        description = self.cleaned_data['description']
        contractType = self.cleaned_data['contractType']
        # Passando os valores para o método create_contract
        contract_instance.create_contract(name, symbol, description, contractType)
        self.contractAddress = contract_instance.contractAddress
        self.contractId = contract_instance.contractId
        super().save(*args, **kwargs)  # Salva a instância do modelo OpenWallet no banco de dados

class Token(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    maxSupply = models.IntegerField()
    description = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=10000)

    def save(self, *args, **kwargs):
        # Antes de salvar, obtenha o projeto associado ao usuário
        project_instance = self.user.project   
        contract_instance = contract.Contract(project_instance) 
        name = self.cleaned_data['name']
        maxSupply = self.cleaned_data['maxSupply']
        description = self.cleaned_data['description']
        imageUrl = self.cleaned_data['imageUrl']
        # Passando os valores para o método create_contract
        contract_instance.create_token(name, description, maxSupply, imageUrl)
        self.contractAddress = contract_instance.contractAddress
        self.contractId = contract_instance.contractId
        super().save(*args, **kwargs)  # Salva a instância do modelo OpenWallet no banco de dados

class Bet(models.Model):
    player1 = models.CharField(max_length=100, blank=True)
    player2 = models.CharField(max_length=100, blank=True)

class Athlete(models.Model):
    athleteName = models.CharField(max_length=100)
    athleteId = models.IntegerField()
    
class Experience(models.Model):
    experienceId = models.IntegerField()
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    experienceName = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    imageUrl = models.CharField(max_length=10000)
    flag = models.CharField(max_length=10)
    price = models.IntegerField()