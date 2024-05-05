from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Wallet, Contract, Athlete, Experience, Token


class AthleteSerializer(ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'

class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['imageUrl', 'description', 'maxSupply', 'name']

class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = 'walletTokens'