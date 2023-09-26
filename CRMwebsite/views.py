from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Cliente


def home(request):
    clientes = Cliente.objects.all()
    
    # Verifica se o usuário esta logando (POSTING)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticando o usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Usuário logado com sucesso!")
            return redirect('home')
        else:
            messages.success(request, "Ocorreu um erro! Por favor Tente novamente....")
            return redirect('home')
    else:
        return render(request, 'home.html', {'clientes':clientes})


def logout_user(request):
    logout(request)
    messages.success(request, "Usuário deslogado com sucesso!")
    return render(request, 'home.html', {})

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Autentica e Loga o Usuário
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Usuário registrado com Sucesso!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
        
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Exibe o cadastro
        customer_record = Cliente.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "Você precisa estar logado para acessar a página de cadastros!")
        return redirect('home')