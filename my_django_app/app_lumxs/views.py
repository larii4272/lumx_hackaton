from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app_lumxs.models import CustomUser, Wallet
from app_lumxs.forms import CreateContract
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    """Página principal"""
    return render(request, 'index.html')
