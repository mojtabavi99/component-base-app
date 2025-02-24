from django.contrib import admin

from plugin_billboard import models

admin.site.register(models.Billboard)
admin.site.register(models.BillboardItem)