from django.db import models

# Create your models here.

class Divisions(models.Model):
    name = models.CharField(max_length = 400)
