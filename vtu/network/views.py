from select import select
from django.shortcuts import render
from django.http import JsonResponse
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

def get_vtu(phone, code ):
    """Makes API calls to https://api.fastmobiledeals.com.ng/documentation/index.php#codes"""
    TEST_API_KEY= "FmD_test_AaCMsGmw9rkEqthI64HBW1czVX0pZd2DKOuUgnNf"
    ACCOUNT_TOKEN= "EQL6CzdNVXrIYHpj4vgUhscbAWmliefOTk93Rqao"
    DATA_PLAN_CODE= code
    RECIEPIENT_NUMBER= phone
    UNIQUE_REFERENCE= "ABCD1234"
    url = f'https://api.fastmobiledeals.com.ng/API/test_box/mtnGifting?apiToken={TEST_API_KEY}&mobilenumber={RECIEPIENT_NUMBER}&planCode={DATA_PLAN_CODE}&ref={UNIQUE_REFERENCE}&clientToken={ACCOUNT_TOKEN}'
    
    return requests.get(url).json()

def handleData(request):
    if request.method == 'POST':
        form = mtn(request.POST)
        if form.is_valid():
            phone=form.cleaned_data['phone']
            volume_field= form.cleaned_data['volume_field']
            submit = MTN(volume_field= volume_field , phone= phone)
            submit.save()

        vtu= get_vtu(phone, volume_field)
        return JsonResponse(vtu)
    else:
        form= mtn()
        context={'form': form }
        return render(request, 'network/mtn.html', context)
            
        # apiResponse = {}
        # if apiResponse.success : 
        #     return render(request, 'recharge_success.html')
        # else:
        #     reason = apiResponse.reason
        
