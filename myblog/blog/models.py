from django.db import models

class Atricle(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)