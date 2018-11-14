from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pud_date = models.DateTimeField()
    body = models.TextField(default='')
    image = models.ImageField(upload_to='images/')
