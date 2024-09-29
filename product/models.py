from django.db import models
from django.conf import settings
from django.utils.deconstruct import deconstructible
from storages.backends.s3boto3 import S3Boto3Storage

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    available = models.BooleanField(default=True)
    class Meta:
        db_table = 'product' 
    
    def __str__(self):
        return self.product_name
    
    def delete_image(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
  

