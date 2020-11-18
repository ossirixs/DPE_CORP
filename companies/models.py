#Django.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Company(models.Model):
  """Companies Model."""

  name = models.CharField(max_length=255, blank=True)
  address = models.CharField(max_length=255, blank=True)
  phone = models.CharField(max_length=255, blank=True)
  email = models.CharField(max_length=255, blank=True)


  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)


