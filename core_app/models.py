from django.db import models

class File(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')