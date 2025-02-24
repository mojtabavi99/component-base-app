from django.contrib import admin

from plugin_catalog import models

admin.site.register(models.Catalog)
admin.site.register(models.CatalogItem)
