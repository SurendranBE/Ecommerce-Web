from django.db import models
from django.conf import settings
from django.utils.deconstruct import deconstructible
from storages.backends.s3boto3 import S3Boto3Storage
# Create your models here. 

class Category(models.Model):
	category_name 		= models.CharField(max_length=100, blank=True, null=True)
	sort_order 			= models.IntegerField(blank=True, null=True)
	description 		= models.TextField(blank=True, null=True)
	url 				= models.CharField(max_length=100, blank=True, null=True)
	meta_title 			= models.CharField(max_length=100, blank=True, null=True)
	meta_keyword 		= models.CharField(max_length=100, blank=True, null=True)
	meta_content 		= models.CharField(max_length=100, blank=True, null=True)
	image 				= models.ImageField(upload_to='media/')
	banner_img 			= models.ImageField(upload_to='media/')
	draft_status 		= models.IntegerField(blank=True, null=True)
	visibility 			= models.IntegerField(blank=True, null=True, default=1)
	approve 			= models.IntegerField(blank=True, null=True, default=0)
	status 				= models.IntegerField(blank=True, null=True, default=0)
	created_at 			= models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_at 			= models.DateTimeField(auto_now=True, blank=True, null=True)
	class Meta:
		db_table = 'category'
	def __str__(self):
		return self.category_name
	def delete_image(self, *args, **kwargs):
		self.image.delete()
		super().delete(*args, **kwargs)
	def delete_banner(self, *args, **kwargs):
		self.banner_img.delete()
		super().delete(*args, **kwargs)