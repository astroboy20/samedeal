from dataclasses import fields
from django import forms

volume = [
        {'5000', '5GB 10,000'},
        {'3000', '3GB 10,000'},
        {'2000', '2GB 10,000'},
        {'1000', '1GB 10,000'},
        {'500', '500MB 10,000'},
]
    
    
class mtn(forms.Form):
    volume_field = forms.ChoiceField(choices=volume, label='sele ct options')
    phone = forms.IntegerField()
    
    
    
class glo(forms.ModelForm):
    phone = forms.IntegerField()
    
    amount = forms.IntegerField()  
    
class airtel(forms.ModelForm):
   phone = forms.IntegerField()
   amount = forms.IntegerField()
    
class mobile(forms.ModelForm):
    phone = forms.IntegerField()
    
    amount = forms.IntegerField()    
    
