from django import forms

class Contact(forms.Form):
    Name = forms.Field(widget= forms.TextInput(attrs={
        "class":"control ", 'placeholder':"Full Name"
    }))
    
    Email = forms.Field(widget=forms.EmailInput(attrs={
        "class":"control", 'placeholder':"Email"}))  
    
    
    Message = forms.Field(widget=forms.Textarea(attrs={
        "class":"control ", 'placeholder':"Message"
    }))