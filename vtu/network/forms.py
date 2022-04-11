from django import forms

MTN_DATA_PLAN = (
        ('5000', '5GB 10,000'),
        ('3000',' 3GB 10,000'),
        ('2000','2GB 10,000'),
        ('1000','1GB 10,000'),
        ('500','500MB 10,000'),
)

AIRTEL_DATA_PLAN = (
        ('606', '5GB 10,000'),
        ('605',' 3GB 10,000'),
        ('604','2GB 10,000'),
        ('603','1GB 10,000'),
        ('602','500MB 10,000'),
)



class MTNnetwork(forms.Form):
    mtn_data_plan = forms.ChoiceField(choices=MTN_DATA_PLAN) 
    phone_number = forms.IntegerField()

class AIRTELnetwork(forms.Form):
    airtel_data_plan = forms.ChoiceField(choices=AIRTEL_DATA_PLAN) 
    phone_number = forms.IntegerField()

class glo(forms.ModelForm):
    phone = forms.IntegerField()
    
    amount = forms.IntegerField()  
    


    
class mobile(forms.ModelForm):
    phone = forms.IntegerField()
    
    amount = forms.IntegerField()    
    
