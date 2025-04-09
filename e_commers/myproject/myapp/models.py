from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(default='',blank=True,null=True)
    phone=models.IntegerField(max_length=15)
    city=models.CharField(max_length=100)
    model=models.CharField(max_length=10)
    color=models.CharField(max_length=10)  
    def __str__(self):
        return self.name 
