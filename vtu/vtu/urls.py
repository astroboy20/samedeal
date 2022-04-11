"""vtu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from Logic.views import home

from django.contrib.auth import views as auth_views

from Users.views import register, Login,logout, reset, dashboard, transaction

from network.views import handleMTNdata, handleAIRTELdata
from paystack.views import initiate_payment, verify_payment



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',Login,name='login'),
    path('logout/',logout,name='logout'),
    path('reset/',reset,name='reset'),
    path('dashboard/',dashboard,name='dashboard'),
    path('transaction/',transaction,name='transaction'),
    path('handleMTNdata/',handleMTNdata,name='handleMTNdata'),
    path('handleAIRTELdata/',handleAIRTELdata,name='handleAIRTELdata'),
    #path('handleGLOdata/',handleGLOdata,name='handleGLOdata'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('initiate_payment/',initiate_payment ,name='initiate_payment'), 
    path('<str:ref>/', verify_payment ,name='verify-payment'),
    
    
]
