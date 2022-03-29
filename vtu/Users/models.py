from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    balance = models.IntegerField( blank = False, default=0.0)


    
class Order(models.Model):
    user = models.ForeignKey (get_user_model(), on_delete=models.CASCADE, blank=False )
    amount = models.CharField(max_length=12)
    tx_ref =models.CharField(max_length=256, unique=True)
    is_settled=models.BooleanField(default=False)
    
    def __str__(self) :
        return self.id