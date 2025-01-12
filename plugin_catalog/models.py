from django.db import models

from app_core.models import Page


class Catalog(models.Model):
    MODEL_ARTICLE = 'article'
    MODEL_PRODUCT = 'product'
    MODEL_CHOICES = (
        (MODEL_ARTICLE, 'مقاله'),
        (MODEL_PRODUCT, 'محصول'),
    )
    TYPE_LIST = 'list'
    TYPE_GRID = 'grid'
    TYPE_CHOICES = (
        (TYPE_LIST, 'لیست'),
        (TYPE_GRID, 'گرید'),
    )
    GENERATED_AUTO = 'auto'
    GENERATED_MANUAL = 'manual'
    GENERATED_CHOICES = (
        (GENERATED_AUTO, 'خودکار'),
        (GENERATED_MANUAL, 'دستی'),
    )

    name = models.CharField(max_length=255, verbose_name='نام کاتالوگ')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    model = models.CharField(max_length=255, choices=MODEL_CHOICES, verbose_name='مدل')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع کاتالوگ')
    generated = models.CharField(max_length=255, choices=GENERATED_CHOICES, verbose_name='روش تولید')
    see_all_link = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینک موارد بیشتر')
    max_items = models.IntegerField(default=0, verbose_name='حداکثر تعداد')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')

    class Meta:
        verbose_name = 'کاتالوگ'
        verbose_name_plural = 'لیست کاتالوگ‌ها'

    def __str__(self):
        return self.name


class CatalogItem(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='شناسه مجموعه')
    item = models.IntegerField(verbose_name='شناسه آیتم')

    class Meta:
        verbose_name = 'اجزا کاتالوگ'
        verbose_name_plural = 'لیست اجزا کاتالوگ'

    def __str__(self):
        return f'{self.catalog.name} - {self.item}'
