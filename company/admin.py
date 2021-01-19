#Django.
from django.contrib import admin
#Company.
from .models import Company, CompanyTest, TestCode

admin.site.register(Company)
admin.site.register(CompanyTest)
admin.site.register(TestCode)