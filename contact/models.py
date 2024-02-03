from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Information(models.Model):
    address=models.CharField(max_length=100)
    streat= models.CharField(max_length=100)
    phone=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.email

    class Meta:
        db_table='information'
        verbose_name="Site Information"

