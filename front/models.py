from django.db import models

class Author(models.Model):
    username=models.CharField(max_length=100,null=False)