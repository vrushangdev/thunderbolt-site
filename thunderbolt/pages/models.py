from django.db import models
from datetime import  datetime
# Create your models here.
class TeamMembers(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    github = models.CharField(max_length=300,blank=True)
    linkedin = models.CharField(max_length=300,blank=True)
    photo_main = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name
class Advisors(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    github = models.CharField(max_length=300,blank=True)
    linkedin = models.CharField(max_length=300,blank=True)
    photo_main = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Roadmap(models.Model):
    completion_date = models.DateField(default=datetime.now,blank=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return  self.details

class Sponsors(models.Model):
    name = models.TextField(max_length=50,blank=True)
    description = models.TextField(blank=True)
    link = models.TextField(max_length=300,blank=True)
    img = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Usecase(models.Model):
    title = models.CharField(max_length=300,blank=True)
    desc = models.TextField(blank=True)
    uimg = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return  self.title