from django.db import models

# Create your models here.
class Questions(models.Model):
    searchTerm=models.JSONField()
    searchResult=models.JSONField()