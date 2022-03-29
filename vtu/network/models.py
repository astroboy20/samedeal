from django.db import models


volume = [
        ('1', '5GB 10,000'),
        ('2',' 3GB 10,000'),
        ('3','2GB 10,000'),
        ('4','1GB 10,000'),
        ('5','500MB 10,000'),
]

# Create your models here.
class MTN(models.Model):
    volume_field = models.CharField(max_length=20, choices=volume, default=1) 
    phone =models.PositiveIntegerField()
    
     
    
    
class AIRTEL(models.Model):
    amount =models.PositiveIntegerField()
    phone =models.PositiveIntegerField()
    
class GLO(models.Model):
    amount =models.PositiveIntegerField()
    phone =models.PositiveIntegerField()
    
class MOBILE(models.Model):
    amount =models.PositiveIntegerField()
    phone =models.PositiveIntegerField()