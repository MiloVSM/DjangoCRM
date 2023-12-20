from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obrigatório. Apenas Letras, digitos e @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não deve conter informações comuns como o seu nome ou data de nascimento.</li><li>Sua senha deve conter no mínimo 8 caracteres</li><li>Sua senha não pode ser uma senha comum.</li><li>Sua senha não pode conter apenas números.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repita a Senha'
        self.fields['password2'].label = ''


# Criar formulário para Adicionar Clientes
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Nome", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Sobrenome", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Email", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Telefone", "class": "form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Endereço", "class": "form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Cidade", "class": "form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Estado", "class": "form-control"}), label="")
    cep = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "CEP", "class": "form-control"}), label="")

    class Meta:
        model = Cliente
        exclude = ('user',)
