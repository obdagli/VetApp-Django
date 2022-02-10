from pydoc import describe
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class Owner(models.Model):
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    def __str__(self):
        return str(self.firstname)

class PetOwnerMatching(models.Model):
    ownerid = models.ForeignKey(Owner, on_delete=models.CASCADE)
    petid = models.ForeignKey(Pet, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
