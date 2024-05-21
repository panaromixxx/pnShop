from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=59)
    discription = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/")
    rating = models.PositiveBigIntegerField()
    discount = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)