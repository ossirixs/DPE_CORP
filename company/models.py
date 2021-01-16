#Django.
from django.db import models
from django.urls import reverse
#Models.
from users.models import User
from tests.models import TestCatalog

class Company(models.Model):
    """
    Companies Model.
    """

    COMPANY_TYPE = [
        ('MAIN', 'Main'),
        ('BRANCH', 'Branch'),
    ]


    company_type = models.CharField(max_length=10,choices=COMPANY_TYPE,default='MAIN')
    company_name = models.CharField(max_length=255, blank=True)
    company_contact = models.CharField(max_length=255, blank=True)
    company_phone = models.CharField(max_length=255, blank=True)
    company_email = models.CharField(max_length=255, blank=True)
    # The id of the company this company belongs to, in case this is a sub company or branch
    company_main = models.IntegerField(blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class TestCode(models.Model):
    """Test codes model."""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    test = models.CharField(max_length=25)
    code = models.CharField(max_length=40)
    creation = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    expiration = models.DateField()

class CompanyTest(models.Model):
    """
    Model to make the relation between the companies and their asigned tests.
    """
    company =  models.ForeignKey(Company, on_delete=models.CASCADE)
    test = models.ForeignKey(TestCatalog, on_delete=models.CASCADE)

