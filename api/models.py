from django.db import models
from account.models import User

# Create your models here.
class Master(models.Model):
    national_code = models.ForeignKey(User,on_delete=models.CASCADE)


class Gym(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    national_code = models.ForeignKey(User,on_delete=models.CASCADE)


class Student(models.Model):
    national_code = models.ForeignKey(User,on_delete=models.CASCADE)
    master_national_code = models.ForeignKey(Master,on_delete=models.CASCADE)
    gym_id = models.ForeignKey(Gym,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.national_code__username