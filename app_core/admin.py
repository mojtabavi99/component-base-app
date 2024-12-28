from django.contrib import admin
from app_core import models

admin.site.register(models.Config)
admin.site.register(models.Province)
admin.site.register(models.City)
