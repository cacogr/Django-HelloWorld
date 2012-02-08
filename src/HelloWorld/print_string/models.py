from django.db import models

class HelloWorld(models.Model):
    string = models.CharField(max_length=255)
