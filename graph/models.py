from django.db import models
from django.urls import reverse

# Create your models here.

class ExcelFile(models.Model):
    file = models.FileField(upload_to = "graph/static/graph/")
