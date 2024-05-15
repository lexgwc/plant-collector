from django.contrib import admin
# import your models here
from .models import Plant, Watering, Tool

# Register your models here
admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Tool)

