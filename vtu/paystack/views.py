from multiprocessing import context
from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PaymentForm
from django.conf import settings
from .models import Payment
from django.contrib import messages
from Users.models import Order
# Create your views here.
def initiate_payment(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            print(settings.PAYSTACK_PUBLIC_KEY)
            return render(request, 'paystack/make_payment.html', {'payment':payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = PaymentForm()
    return  render(request, 'paystack/initiate_payment.html', {'payment_form': payment_form})

def verify_payment(request:HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref) 
    verified =  payment.verify_payment()
    
    
    if verified:
        messages.success(request, 'verification successful')
    
        
    else:  
        messages.error(request, "Verification failed")
        return redirect( 'dashboard')
        