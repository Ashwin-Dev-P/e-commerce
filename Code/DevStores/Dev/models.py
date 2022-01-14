from django.db import models
from django import forms

# Create your models here.
class dress(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    
class customer_review(models.Model):
    product = models.ForeignKey(dress,default=None,on_delete=models.CASCADE,)
    review = models.CharField(max_length=500)
    
        
