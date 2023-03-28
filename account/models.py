from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    national_code = models.CharField(max_length=10,
                                     primary_key=True,
                                     unique=True)
    mobile_no = models.CharField(max_length=11,unique=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
