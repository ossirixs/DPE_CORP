# Django
from django.contrib import admin

# Models
from company.models import TestCatalog
from .models import MaxPositions

admin.site.register(TestCatalog)

class MaxPositionsAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'created')
    list_display_links = list_display
admin.site.register(MaxPositions, MaxPositionsAdmin)