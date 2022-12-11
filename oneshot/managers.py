from django.db import models

class CartManager(models.Manager):
    def create_cart(self,user):
        cart = self.create(user=user)
        return cart