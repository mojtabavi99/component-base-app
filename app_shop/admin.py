from django.contrib import admin
from app_shop import models

admin.site.register(models.Product)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductSpec)
admin.site.register(models.ProductGallery)
admin.site.register(models.ProductCategory)
