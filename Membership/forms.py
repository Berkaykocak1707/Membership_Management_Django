from django.contrib.auth.forms import UserCreationForm , SetPasswordForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import widgets
from django import forms

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email",)
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields["email"].required = True

    def clean_email(self):
     email = self.cleaned_data.get("email")
     if User.objects.filter(email = email).exists():
        self.add_error("email","email is unavailable")

class EmailPasswordUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['email', 'password']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match')
        return cleaned_data


class PasswordUpdateForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Confirm new password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    