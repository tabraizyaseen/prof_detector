from django.db import models

# Create your models here.

class Upload(models.Model):
	image = models.ImageField(upload_to='images')

	class Meta:
		verbose_name_plural="Image Upload"
