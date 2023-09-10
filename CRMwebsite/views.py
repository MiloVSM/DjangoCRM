from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # Verifica se o usuário esta logando (POSTING)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Autenticando o usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Usuário logado com sucesso!")
            return redirect('home')
        else:
            messages.success(
                request, "Ocorreu um erro! Por favor Tente novamente...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Usuário deslogado com sucesso!")
    return render(request, 'home.html', {})
