#Django.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """ Admin & Client models based on the 
    Users model. """

    class Types (models.TextChoices):
        ADMIN_DPE = "ADMIN_DPE", "Administrador DEP"
        CLIENT_MAIN = "CLIENT_MAIN", "Cliente Matriz"
        CLIENT = "CLIENT", "Cliente Sucursal"
    #General.
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.CLIENT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(_('Name of user'),max_length=250, blank=True)
    second_last_name = models.CharField(_('Second Last Name'),max_length=250, blank=True,null=True)
    #Clients.
    company = models.IntegerField(_('Company'), blank=True,null=True)
    company_main = models.IntegerField(_('Main Company'), blank=True,default=0)
    uci = models.CharField(_('Company identifier'), max_length=255, blank=True) # Unique Company Identifier LoL

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
