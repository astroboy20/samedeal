import secrets
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
    ref =models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.mtn_data_plan

    
class AIRTEL(models.Model):
    airtel_data_plan = models.CharField(max_length=20, choices=AIRTEL_DATA_PLAN) 
    phone_number = models.IntegerField()
    ref =models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.airtel_data_plan
    
    def save(self, *args ,**kwargs) -> None:
        while not self.ref:
            ref =secrets.token_urlsafe(50)
            object_with_similar_ref = AIRTEL.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref =ref
        super().save(*args, **kwargs)
    
class GLO(models.Model):
    amount =models.PositiveIntegerField()
    phone =models.PositiveIntegerField()
    
class MOBILE(models.Model):
    amount =models.PositiveIntegerField()
    phone =models.PositiveIntegerField()