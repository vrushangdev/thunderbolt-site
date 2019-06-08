from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=15)
    contact_date = models.DateField(default=datetime.now)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.name
