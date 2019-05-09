from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields=["username",]
        

    
        

