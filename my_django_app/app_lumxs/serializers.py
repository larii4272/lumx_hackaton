from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Wallet, Contract, Athlete, Experience


class AthleteSerializer(ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'

class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'