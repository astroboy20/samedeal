from select import select
from django.shortcuts import render
from .forms import mtn,glo,airtel,mobile
from .models import MTN,GLO,AIRTEL,MOBILE
import requests
import json

# # Create your views here.
# def mtn(request):
#     return render(request, 'network/mtn.html')
# def glo(request):
#     return render(request, 'network/glo.html')
# def mobile(request):
#     return render(request, 'network/9mobile.html')
# def airtel(request):
#     return render(request:, 'network/airtel.html')
def handleData(request):
    form = mtn(request.POST)
    if form.is_valid():
        submit = MTN(volume_field = form.cleaned_data['volume_field'],
                    phone=form.cleaned_data['phone']
                        
                        )
        submit.save()
        print(select)
    context={
        'form': form
    }
    return render(request, 'network/mtn.html', context)
        
        # apiResponse = {}
        # if apiResponse.success : 
        #     return render(request, 'recharge_success.html')
        # else:
        #     reason = apiResponse.reason
        
    