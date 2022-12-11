from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .managers import CartManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)



class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()

    @classmethod
    #stores even when no instance
    def updateprice(cls,product_id,price):
        #product=get_object_or_404(cls,product_id=product_id)
        product=cls.objects.get(id=product_id)
        print(product)
        product.price = price
        product.save()
    """
    #uses self/so atleast 1 instance/object is required
    def updateprice(self,price):
        self.price =price
        self.price.save()
    """

    def __str__(self):
        return self.name

class Cart(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    objects=CartManager()

    def __str__(self):
        return str(self.user)
