from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Billboard(models.Model):
    TYPE_SLIDER = 'slider'
    TYPE_BANNER = 'banner'
    TYPE_POSTER = 'poster'
    TYPE_CHOICES = (
        (TYPE_SLIDER, 'اسلایدر'),
        (TYPE_BANNER, 'بنر'),
        (TYPE_POSTER, 'پوستر')
    )

    POSITION_TOP = 'top'
    POSITION_MID = 'middle'
    POSITION_BOT = 'bottom'
    POSITION_CHOICES = (
        (POSITION_TOP, 'بالا'),
        (POSITION_MID, 'میانه'),
        (POSITION_BOT, 'پایین'),
    )
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISH = 'publish'
    STATUS_INVISIBLE = 'invisible'
    STATUS_CHOICES = (
        (STATUS_DRAFT, 'در صف انتشار'),
        (STATUS_PUBLISH, 'منتشر شده'),
        (STATUS_INVISIBLE, 'پنهان شده'),
    )

    link = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینک')
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name='کپشن')
    image_desktop = models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (دسکتاپ)')
    image_tablet = models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (تبلت)')
    image_mobile = models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (موبایل)')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیحات تصویر')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع')
    position = models.CharField(max_length=255, choices=POSITION_CHOICES, default=POSITION_TOP, verbose_name='موقعیت')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_DRAFT, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'بیلبورد'
        verbose_name_plural = 'بیلبوردها'

    def __str__(self):
        return self.link


class Meta(models.Model):
    META_TYPE = (
        ('rel', 'rel'),
        ('name', 'name'),
        ('property', 'property')
    )

    type = models.CharField(max_length=255, choices=META_TYPE, verbose_name='نوع تگ')
    keyword = models.CharField(max_length=255, verbose_name='کلیدواژه')
    content = models.CharField(max_length=255, verbose_name='محتوا')

    class Meta:
        verbose_name = 'متا تگ'
        verbose_name_plural = 'متا تگ‌ها'

    def __str__(self):
        return self.keyword


class Faq(models.Model):
    SUBJECT_PURCHASE = 'purchase'
    SUBJECT_COURIER = 'courier'
    SUBJECT_REGISTRATION = 'registration'
    SUBJECT_CHOICES = (
        (SUBJECT_PURCHASE, 'خرید'),
        (SUBJECT_COURIER, 'ارسال مرسولات'),
        (SUBJECT_REGISTRATION, 'ثبت نام'),
    )

    subject = models.CharField(max_length=255, choices=SUBJECT_CHOICES, verbose_name='موضوع')
    order = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name='ترتیب نمایش')
    question = models.CharField(max_length=255, verbose_name='سوال')
    answer = models.TextField(verbose_name='پاسخ')

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'

    def __str__(self):
        return f"{self.subject} - {self.question}"
