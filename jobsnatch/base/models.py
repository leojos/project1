from django.db import models
from django.contrib.auth.models import User

class displayusername(models.Model):
  username = models.CharField(max_length=255)

class tblcomp(models.Model):
  username = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length = 254)
  password = models.CharField(max_length=20)

class reg(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  usertype=models.CharField(max_length=255)
  def __str__(self):
    return self.user.username