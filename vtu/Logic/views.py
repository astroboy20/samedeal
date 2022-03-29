from django.shortcuts import render
from .models import Contactform
from .form import Contact
from  django.contrib import messages
import requests

# Create your views here.
def home(request):
    form = Contact(request.POST)
    if form.is_valid():
        submit = Contactform(Fullname=form.cleaned_data['Name'],
                        Email = form.cleaned_data['Email'],
                        Message =form.cleaned_data['Message'],)
        submit.save()
        messages.success(request, f'message sent')

    context = {
        'form':form,
        'title': 'Samedeal | Home '
        
    }
    
    #response = requests.get('https://jsonplaceholder.typicode.com/users')
    return render(request, 'index.html', context)