from django.db import models

class Config(models.Model):
    site_title = models.CharField(max_length=255, verbose_name='عنوان سایت')
    site_name = models.CharField(max_length=255, verbose_name='نام سایت')
    site_description = models.CharField(max_length=255, verbose_name='نوضیحات سایت')
    slogan = models.CharField(max_length=255, verbose_name='شعار سایت')
    logo = models.ImageField(upload_to='images/core/config/', verbose_name='لوگو')
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='تلفن')
    mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name='موبایل')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='آدرس')
    instagram = models.CharField(max_length=255, blank=True, null=True, verbose_name='اینستاگرام')
    facebook = models.CharField(max_length=255, blank=True, null=True, verbose_name='فیسبوک')
    telegram = models.CharField(max_length=255, blank=True, null=True, verbose_name='تلگرام')
    twitter = models.CharField(max_length=255, blank=True, null=True, verbose_name='توییتر')
    whatsapp = models.CharField(max_length=255, blank=True, null=True, verbose_name='واتساپ')
    linkedin = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینکدین')
    youtube = models.CharField(max_length=255, blank=True, null=True, verbose_name='یوتیوب')
    aparat = models.CharField(max_length=255, blank=True, null=True, verbose_name='آپارات')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name

