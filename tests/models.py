from django.db import models

class User (models.Model):
  """User model."""
  email = models.EmailField()
  password = models.CharField()

  first_name = models.CharField()
  last_name = models.CharField()

