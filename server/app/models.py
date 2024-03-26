from django.db import models

from django.db import models

class UploadedImages(models.Model):
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    # Add other fields if needed for storing model predictions, etc.