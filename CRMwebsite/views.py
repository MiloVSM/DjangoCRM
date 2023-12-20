from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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
            messages.success(
                request, "Ocorreu um erro! Por favor Tente novamente....")
            return redirect('home')
    else:
        return render(request, 'home.html', {'clientes': clientes})


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
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Exibe o cadastro
        customer_record = Cliente.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(
            request, "Você precisa estar logado para acessar a página de cadastros!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Cliente.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Usuário deletado com sucesso!")
        return redirect('home')
    else:
        messages.success(
            request, "Você precisa estar logado para acessar manipular dados!")
        return redirect('home')
    
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Cliente cadastrado com sucesso!")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Você precisa estar logado para acessar está página!")
		return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Cliente.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro de cliente atualizado!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Você precisa estar logado para acessar está página!")
        return redirect('home')
