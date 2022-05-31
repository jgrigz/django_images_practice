from django.db import models

# Create your models here.
class Image(models.Model):
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")