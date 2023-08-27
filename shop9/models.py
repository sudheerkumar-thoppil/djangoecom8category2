from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    price =models.IntegerField()
    image = models.ImageField(upload_to ='media')

    def __str__(self):
        return self.name

