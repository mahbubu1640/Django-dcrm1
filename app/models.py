from django.db import models

# created_at / first_name / last_name/email/phone / address / city / zipcode 


class Record(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    