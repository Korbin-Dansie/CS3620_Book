from django.db import models

# Create your models here.
class BookData(models.Model):
    name  = models.CharField(max_length=256)
    category  = models.CharField(max_length=64)
    description  = models.TextField(max_length=1024)
    rating  = models.FloatField()
    image  = models.ImageField(default="NoImage.jpg")

    def __str__(self):
        return self.name