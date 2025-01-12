from django.db import models

from app_core.models import Page

class MetaTag(models.Model):
    TYPE_REL = 'rel'
    TYPE_NAME = 'name'
    TYPE_PROPERTY = 'property'
    TYPE_CHOICES = (
        (TYPE_REL, TYPE_REL),
        (TYPE_NAME, TYPE_NAME),
        (TYPE_PROPERTY, TYPE_PROPERTY)
    )

    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع تگ')
    keyword = models.CharField(max_length=255, verbose_name='کلیدواژه')
    content = models.CharField(max_length=255, verbose_name='محتوا')

    class Meta:
        verbose_name = 'متا تگ'
        verbose_name_plural = 'متا تگ‌ها'

    def __str__(self):
        return f'{self.keyword} ({self.content})'