from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=244)
    first_name = models.CharField(max_length=244)
    last_name = models.CharField(max_length=244)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=244)
    created_at = models.DateField(auto_created=True, auto_now=True)
    is_Active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class ProductsModel(models.Model):
    product_name = models.CharField(max_length=244)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/')
    product_created_at = models.DateField(auto_created=True, auto_now=True)
    product_added_by = models.CharField(default="Admin",max_length=244)


    def __str__(self):
        return self.product_name
