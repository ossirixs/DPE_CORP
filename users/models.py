#Django.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """ Admin & Client models based on the 
    Users model. """

    class Types (models.TextChoices):
        ADMIN_DPE = "ADMIN_DPE", "Admin_dpe"
        CLIENT_MAIN = "CLIENT_MAIN", "Client_main"
        CLIENT = "CLIENT", "Client"
    #General.
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.CLIENT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(_('Name of user'),max_length=250, blank=True)
    #Clients.
    company = models.CharField(_('Company'), max_length=255, blank=True)
    uci = models.CharField(_('Company identifier'), max_length=255, blank=True) # Unique Company Identifier LoL

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

# Proxy Managers.
class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=User.Types.ADMIN_DPE)

class ClientMainManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=User.Types.CLIENT_MAIN)

class ClientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=User.Types.CLIENT)

#Proxy User types.
class AdminDPE(User):
    objects = AdminManager()

    class Meta:
        proxy = True

    # Additional methods for AdminDPE

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN_DPE
        return super().save(*args, **kwargs)

class ClientMain(User):
    objects = ClientMainManager()

    class Meta:
        proxy = True

     # Additional methods for ClientMain

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CLIENT_MAIN
        return super().save(*args, **kwargs)

class Client(User):
    objects = ClientManager()

    class Meta:
        proxy = True

     # Additional methods for Client

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CLIENT
        return super().save(*args, **kwargs)