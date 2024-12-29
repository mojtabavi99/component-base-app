from django.contrib import admin
from app_user import models

admin.site.register(models.User)
admin.site.register(models.Address)
admin.site.register(models.VerifyToken)
