from .models import CustomUser
from django import forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','username', 'email', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'required' : '', 'Placeholder' : 'Username'}),
            'first_name' : forms.TextInput(attrs={'required' : '', 'Placeholder' : 'First name'}),
            'last_name' : forms.TextInput(attrs={'required' : '', 'Placeholder' : 'Last name'}),
            'email' : forms.EmailInput(attrs={'required' : '', 'Placeholder' : 'Email'}),
            'password' : forms.PasswordInput(attrs={'required' : '', 'Placeholder' : 'Password'}),
        }
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'required' : '', 'Placeholder' : 'Username'}),
            'password' : forms.PasswordInput(attrs={'required' : '', 'Placeholder' : 'Password'}),
        }