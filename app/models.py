from django.db import models

class File(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to="files",max_length=250)
    text = models.CharField(max_length=5000, default="Blank Pdf")
