from django.db import models
from django.urls import reverse
import os.path
# Create your models here.


def update_filename(instance, filename):
    path = "graph/static/graph/"
    format = "Uploaded_Data.xlxs"
    return os.path.join(path, format)

class ExcelFile(models.Model):
    file = models.FileField(upload_to = "graph/static/graph/")

    def filename(self):
        return os.path.basename(self.file.name)
