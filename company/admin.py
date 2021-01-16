#Django.
from django.contrib import admin
#Company.
from .models import Company, CompanyTest

admin.site.register(Company)
admin.site.register(CompanyTest)