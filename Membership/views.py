from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm, SetPasswordForm
from Membership.forms import EmailPasswordUpdateForm, NewUserForm, PasswordUpdateForm
from social_django.models import UserSocialAuth
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordResetForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator

def login_site(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Perfect!")
                nextUrl = request.GET.get("next",None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                form = AuthenticationForm(request,data=request.POST)
                return render(request, 'login.html',{"form":form})    
        else:
            messages.add_message(request, messages.ERROR, "Username or password is not correct!")
            return render(request, 'login.html',{"form":form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{"form":form})
    
@login_required()
def index(request):
    has_email = bool(request.user.email)
    
    has_password = request.user.has_usable_password()
    
    if not has_email and not has_password:
        return redirect('mail_password_social')
    elif not has_password:
        return redirect('password_social')
    else:
        return render(request, 'index.html',)


@login_required()
def mailpasswordsocial(request):
    if request.method == "POST":
        form = EmailPasswordUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmailPasswordUpdateForm(instance=request.user)
    return render(request, 'mailpasswordsocial.html', {'form': form})

@login_required()
def passwordsocial(request):
    if request.method == "POST":
        form = PasswordUpdateForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordUpdateForm(request.user)
    return render(request, 'passwordsocial.html', {'form': form})

@login_required()
def logout_site(request):
    messages.add_message(request, messages.SUCCESS, "Bye!")
    logout(request)
    return redirect("login_site")

@login_required()
def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_site')
        else:
            return render(request,"signup.html",{"form":form})
    else:
        form = NewUserForm()
        return render(request,"signup.html",{"form":form})


def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': default_token_generator,
                'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
                'email_template_name': 'registration/password_reset_email.html',
                'subject_template_name': 'registration/password_reset_subject.txt',
                'request': request,
            }
            form.save(**opts)
            return HttpResponseRedirect(reverse('password_reset_done'))
    else:
        form = PasswordResetForm()
    return render(request, 'fg_password/forgot_password.html', {'form': form})

class ForgotPasswordView(PasswordResetView):
    template_name = 'fg_password/forgot_password.html'
    email_template_name = 'fg_password/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'fg_password/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'fg_password/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'fg_password/password_reset_complete.html'

@login_required()
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Password updated!")
            return redirect("change_password")
        else:
            return render(request, 'change_password.html',{"form":form})
    else:    
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html',{"form":form})
