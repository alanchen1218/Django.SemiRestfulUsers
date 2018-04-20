from __future__ import unicode_literals
from django.db import models
from .models import *

class UserManager(models.Manager):
    def nameValidation(self,postData):
        print("in nameValidation")
        errors = {}
        if len(postData['fullname']) < 1:
            errors['fullname'] = "Please enter valid name"
        if len(postData['email']) < 1:
            errors['email'] = "Please enter valid email"
        
        return errors

class User(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()