from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
    identifiant = forms.CharField(max_length=5, help_text='Entrez votre identifiant...')
    first_name = forms.CharField(max_length=40, help_text='Entrez votre prénom...')
    last_name = forms.CharField(max_length=40, help_text='Entrez votre nom...')

    class Meta:
        model = Account
        fields = ('identifiant', 'first_name', 'last_name', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('identifiant', 'password')

	def clean(self):
		if self.is_valid():
			identifiant = self.cleaned_data['identifiant']
			password = self.cleaned_data['password']
			if not authenticate(identifiant=identifiant, password=password):
				raise forms.ValidationError("identifiant ou mot de passe invalide!")

