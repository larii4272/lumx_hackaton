from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app_lumxs.models import CustomUser, Wallet
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .serializers import AthleteSerializer, ExperienceSerializer, TokenSerializer, Wallet

from .models import Experience, Athlete, Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


def index(request):
    """Página principal"""
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend') 
            return redirect('/')  # Redirect to dashboard or any other page after successful login
        else:
            msg = "Invalid credentials"
            return render(request, 'login.html', {'warning_message': msg})
    else:
        #return redirect(reverse('profile'))
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint': '/notes',
            'method': 'GET',
            'body': None,
            'Description': None
        }
    ]
    return JsonResponse(routes, index=False)


@api_view(['GET'])
def getExperiences(request):
    experiences = Experience.objects.all()
    serializer = ExperienceSerializer(experiences, many=True) #False=> 1 experience, True => more than 1
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getAthletes(request):
    athletes = Athlete.objects.all()
    serializer = AthleteSerializer(athletes, many=True) #False=> 1 experience, True => more than 1
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getTokens(request):
    tokens = Token.objects.all()
    serializer = TokenSerializer(tokens, many=True) #False=> 1 experience, True => more than 1
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getWallet(request):
    wallets = Wallet.objects.all()
    serializer = TokenSerializer(wallets, many=True) #False=> 1 experience, True => more than 1
    return JsonResponse(serializer.data, safe=False)

