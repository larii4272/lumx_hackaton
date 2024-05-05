from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app_lumxs.models import CustomUser, Wallet
from app_lumxs.forms import SolidityCreateToken, CreateAuctionToken
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .serializers import AthleteSerializer, ExperienceSerializer, LumxTokenSerializer, WalletSerializer, SolidityTokenSerializer

from .models import Experience, Athlete, SolidityToken, LumxToken
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
def getLumxTokens(request):
    tokens = LumxToken.objects.all()
    serializer = LumxTokenSerializer(tokens, many=True) #False=> 1 experience, True => more than 1
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getSolidityTokens(request):
    tokens = SolidityToken.objects.all()
    serializer = SolidityTokenSerializer(tokens, many=True) #False=> 1 experience, True => more than 1
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getWallet(request):
    wallets = Wallet.objects.all()
    serializer = WalletSerializer(wallets, many=True) #False=> 1 experience, True => more than 1
    return JsonResponse(serializer.data, safe=False)

def have_experience(request):
    msg = None
    print("Estou dentro da have_experience")
    if request.method == 'POST':
        user = request.POST.get('user')
        experience_id = request.POST.get('experience_id')  # supondo que você tenha um campo no formulário para o ID da experiência
        experience = Experience.objects.get(pk=experience_id)
        wallet = Wallet.objects.get(user=user)  # Supondo que você possa recuperar a carteira do usuário desta maneira
        if wallet.walletTokens >= experience.price:
            # O usuário tem tokens suficientes para comprar a experiência
            # Faça o processamento adicional aqui
            msg = "Compra realizada com sucesso!"
        else:
            # O usuário não tem tokens suficientes
            msg = "Você não tem tokens suficientes para comprar esta experiência."
    return render(request, 'have_experience.html', {'msg': msg})


def create_solidity_token(request):
    if request.method == 'POST':
        form = SolidityCreateToken(request.POST)
        if form.is_valid():
            # Salvando o formulário e processando os dados
            form.save()
            # Redirecionando para uma página de sucesso ou outra página desejada
            return redirect('create_solidity_token')
    else:
        form = SolidityCreateToken()
    
    return render(request, 'create_solidity_token.html', {'form': form})

def create_solidity_auction(request):
    if request.method == 'POST':
        form = CreateAuctionToken(request.POST)
        if form.is_valid():
            # Salvando o formulário e processando os dados
            form.save()
            # Redirecionando para uma página de sucesso ou outra página desejada
            return redirect('create_solidity_auction')
    else:
        form = CreateAuctionToken()
    
    return render(request, 'create_solidity_auction.html', {'form': form})