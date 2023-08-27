from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_site, name='login_site'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_site, name='logout'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot-password/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('changepassword', views.change_password, name='change_password'),
    path('mailpasswordsocial', views.mailpasswordsocial, name='mail_password_social'),
    path('passwordsocial', views.passwordsocial, name='password_social'),
]
