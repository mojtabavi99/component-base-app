from django.contrib import admin
from app_blog import models


admin.site.register(models.Article)
admin.site.register(models.ArticleTag)
admin.site.register(models.ArticleCategory)
