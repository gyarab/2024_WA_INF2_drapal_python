from django.contrib import admin
from content.models import Building, Architect, Style

# Register your models here.

admin.site.register(Building)
admin.site.register(Architect)
admin.site.register(Style)