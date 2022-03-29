from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username' ,'email', 'password1', 'password2']
        
    
    first_name = forms.Field( widget=forms.TextInput(attrs={
        "class":"form-control form-control-user", 'placeholder':"First Name"}))  
    last_name = forms.Field(widget=forms.TextInput(attrs={
        "class":"form-control form-control-user", 'placeholder':"Last Name"}))  
    username = forms.Field(widget=forms.TextInput(attrs={
        "class":"form-control form-control-user", 'placeholder':"UserName"}))  
    email = forms.Field(widget=forms.EmailInput(attrs={
        "class":"form-control form-control-user", 'placeholder':"Email"}))  
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
         "class":"form-control form-control-user", 'placeholder':"Password"}), label="Password")  
    password2 = forms.Field(widget=forms.TextInput(attrs={
         "class":"form-control form-control-user", 'placeholder':"Confirm Password"}), label= "Confirm Password")  
        
    def save(self, commit=True):
        instance =super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance