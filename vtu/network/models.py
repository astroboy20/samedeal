from django.db import models



MTN_DATA_PLAN = [
        ('5000', '5GB 10,000'),
        ('3000',' 3GB 10,000'),
        ('2000','2GB 10,000'),
        ('1000','1GB 10,000'),
        ('500','500MB 10,000'),
]


AIRTEL_DATA_PLAN = (
        ('606', '5GB 10,000'),
        ('605',' 3GB 10,000'),
        ('604','2GB 10,000'),
        ('603','1GB 10,000'),
        ('602','500MB 10,000'),
)


# Create your models here.
class MTN(models.Model):
    mtn_data_plan = models.CharField(max_length=20, choices=MTN_DATA_PLAN) 
    phone_number = models.IntegerField()
    
    def __str__(self) -> str:
        return self.mtn_data_plan

    
class AIRTEL(models.Model):
    airtel_data_plan = models.CharField(max_length=20, choices=AIRTEL_DATA_PLAN) 
    phone_number = models.IntegerField()
    
    def __str__(self) -> str:
        return self.airtel_data_plan
    
class GLO(models.Model):
    amount =models.PositiveIntegerField()
    phone =models.PositiveIntegerField()
    
class MOBILE(models.Model):
    amount =models.PositiveIntegerField()
    phone =models.PositiveIntegerField()