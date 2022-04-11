import code
import random
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import MTNnetwork, AIRTELnetwork
from .models import MTN,AIRTEL
import requests 

def get_data (phone, code): 
    TEST_API_KEY='FmD_test_AaCMsGmw9rkEqthI64HBW1czVX0pZd2DKOuUgnNf'
    ACCOUNT_TOKEN='EQL6CzdNVXrIYHpj4vgUhscbAWmliefOTk93Rqao'
    DATA_PLAN_CODE= code
    RECIEPIENT_NUMBER= phone
    UNIQUE_REFERENCE= random.random()
    url = f'https://api.fastmobiledeals.com.ng/API/test_box/mtnGifting?apiToken={TEST_API_KEY}&mobilenumber={RECIEPIENT_NUMBER}&planCode={DATA_PLAN_CODE}&ref={UNIQUE_REFERENCE}&clientToken={ACCOUNT_TOKEN}'

    return requests.get(url).json()

def handleMTNdata(request):
    if request.method == "POST":
        mtn_network_form = MTNnetwork(request.POST)
        if mtn_network_form.is_valid():
            mtn_data_plan = mtn_network_form.cleaned_data['mtn_data_plan'],
            phone_number = mtn_network_form.cleaned_data['phone_number']
            submit = MTN(mtn_data_plan=mtn_data_plan, phone_number=phone_number)      
            submit.save()
        
        vtu =get_data(mtn_data_plan, phone_number)
        return JsonResponse(vtu)

    else:
        network_form= MTNnetwork()
        context={'network_form': network_form }
        return render(request, 'network/mtn.html', context)


#AIRTEL DATA
def get_airtel_data (phone, code): 
    TEST_API_KEY='FmD_test_AaCMsGmw9rkEqthI64HBW1czVX0pZd2DKOuUgnNf'
    ACCOUNT_TOKEN='EQL6CZDNVXrlYHpj4vgUhscbAWmliefOTk93Rqao'
    DATA_PLAN_CODE= code
    RECIEPIENT_NUMBER= phone
    UNIQUE_REFERENCE= random.random()
    url = f'https://api.fastmobiledeals.com.ng/API/test_box/airtelGifting?apiToken={TEST_API_KEY}&mobilenumber={RECIEPIENT_NUMBER}&planCode={DATA_PLAN_CODE}&ref={UNIQUE_REFERENCE}&clientToken={ACCOUNT_TOKEN}'

    return requests.get(url).json()


def handleAIRTELdata(request):
    if request.method == "POST":
        airtel_network_form = AIRTELnetwork(request.POST)
        if airtel_network_form.is_valid():
            airtel_data_plan = airtel_network_form.cleaned_data['airtel_data_plan'],
            phone_number = airtel_network_form.cleaned_data['phone_number']

            submit = AIRTEL(airtel_data_plan= airtel_data_plan, phone_number=phone_number)  

            submit.save()
        
        vtu =get_data(airtel_data_plan, phone_number)
        return JsonResponse(vtu)

    else:
       airtel_network_form = AIRTELnetwork()
       context = {'airtel_network_form':airtel_network_form}
       return render(request, 'network/airtel.html', context)
   
   
