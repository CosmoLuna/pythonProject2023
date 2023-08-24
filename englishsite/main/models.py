from django.db import models


class Tiles(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='tiles/images/')
    url = models.URLField(blank=True)

