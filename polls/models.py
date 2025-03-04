from django.db import models

class User(models.Model):

    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    element = models.CharField(max_length=30)
    planet = models.CharField(max_length=30)
    incense = models.CharField(max_length=30)
    candle = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)

    source = models.TextField(blank=True, null=True)
    sigil_url = models.URLField(blank=True, null=True) #TODO нтеграция с файловым хранилищем
    appearance = models.TextField()
    service = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    offering = models.TextField()


