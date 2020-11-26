#Django.
from django.db import models

class Company(models.Model):
    """Companies Model."""

    COMPANY_TYPE = [
        ('MAIN', 'Main'),
        ('BRANCH', 'Branch'),
    ]


    company_type = models.CharField(max_length=10,choices=COMPANY_TYPE,default='MAIN')
    company_name = models.CharField(max_length=255, blank=True)
    company_contact = models.CharField(max_length=255, blank=True)
    company_phone = models.CharField(max_length=255, blank=True)
    company_email = models.CharField(max_length=255, blank=True)

    company_main = models.IntegerField(blank=True,null=True)


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


