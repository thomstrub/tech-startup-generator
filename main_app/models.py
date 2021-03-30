from django.db import models

# Create your models here.
class TechWord(models.Model):
    word = models.CharField(max_length=50)
    