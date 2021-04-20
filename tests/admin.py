# Django
from django.contrib import admin

# Models
from company.models import TestCatalog
from .models import MaxPositions, ObjectIntegrity

admin.site.register(TestCatalog)
admin.site.register(ObjectIntegrity)

class MaxPositionsAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'created')
    list_display_links = list_display
admin.site.register(MaxPositions, MaxPositionsAdmin)