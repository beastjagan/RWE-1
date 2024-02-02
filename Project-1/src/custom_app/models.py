from django.db import models

class Bike(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    class Meta:
        app_label = 'custom_app'


