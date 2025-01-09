from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator

from app_core.models import Page

class Billboard(models.Model):
    TYPE_SLIDER = 'slider'
    TYPE_BANNER = 'banner'
    TYPE_POSTER = 'poster'
    TYPE_CHOICES = (
        (TYPE_SLIDER, 'اسلایدر'),
        (TYPE_BANNER, 'بنر'),
        (TYPE_POSTER, 'پوستر')
    )
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISH = 'publish'
    STATUS_INVISIBLE = 'invisible'
    STATUS_CHOICES = (
        (STATUS_DRAFT, 'در صف انتشار'),
        (STATUS_PUBLISH, 'منتشر شده'),
        (STATUS_INVISIBLE, 'پنهان شده'),
    )

    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینک')
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name='کپشن')
    image_desktop = models.ImageField(upload_to='images/plugin/billboard/', verbose_name='تصویر (دسکتاپ)',
                                      validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])])
    image_mobile = models.ImageField(upload_to='images/plugin/billboard/', verbose_name='تصویر (موبایل)', 
                                     validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])])
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیحات تصویر')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_DRAFT, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'بیلبورد'
        verbose_name_plural = 'بیلبوردها'

    def __str__(self):
        return self.link
