# Django
from django.contrib import admin

# Models
from company.models import TestCatalog
from .models import MaxPositions

admin.site.register(TestCatalog)
admin.site.register(MaxPositions)
