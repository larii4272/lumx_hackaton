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


@login_required
def new_wallet(request):
    if request.method == 'POST':
        walletAddress = request.POST.get('walletAddress')
        user = request.user.project
        