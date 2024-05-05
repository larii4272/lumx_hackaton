from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Wallet, Contract, Athlete, Experience, SolidityToken, LumxToken


class AthleteSerializer(ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'

class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class LumxTokenSerializer(ModelSerializer):
    class Meta:
        model = LumxToken
        fields = ['imageUrl', 'description', 'maxSupply', 'name']

class SolidityTokenSerializer(ModelSerializer):
    class Meta:
        model = SolidityToken
        fields = ['imageUrl', 'description', 'maxSupply', 'name']

class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = 'walletTokens'

class SoliditTokenSerializer(ModelSerializer):
    class Meta:
        model = SolidityToken
        fields = '__all__'