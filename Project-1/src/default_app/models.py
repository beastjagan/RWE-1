from django.db import models

class Rider(models.Model):
    name = models.CharField(max_length=255)

