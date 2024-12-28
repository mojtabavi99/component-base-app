from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator 


# class Page(models.Model):
#     name = models.CharField(max_length=255, unique=True, verbose_name='نام صفحه')
#     url = models.CharField(max_length=255, blank=True, null=True, unique=True, verbose_name='url')
#     active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
#     use_in_navbar = models.BooleanField(default=False, verbose_name='استفاده در منو')
#     use_in_footer = models.BooleanField(default=False, verbose_name='استفاده در فوتر')
    
#     class Meta:
#         verbose_name = 'صفحه فرود'
#         verbose_name_plural = 'صفحات فرود'

#     def __str__(self):
#         return self.name
    

# class PageComponent(models.Model):
#     page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="شناسه صفحه")
#     name = models.CharField()
#     order = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name='ترتیب نمایش')
#     type = models.CharField()
#     style = models.CharField()

#     def __str__(self):
#         return self.name

    
class Config(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='عنوان سایت')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='نام سایت')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='نوضیحات سایت')
    slogan = models.CharField(max_length=255, blank=True, null=True, verbose_name='شعار سایت')
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
    logo = models.ImageField(blank=True, null=True, verbose_name='لوگو',
                             upload_to='images/core/config/', default='images/core/config/default.png', 
                             validators=[FileExtensionValidator(['png'])])

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.name
    

# class Meta(models.Model):
#     META_TYPE = (
#         ('rel', 'rel'),
#         ('name', 'name'),
#         ('property', 'property')
#     )

#     type = models.CharField(max_length=255, choices=META_TYPE, verbose_name='نوع تگ')
#     keyword = models.CharField(max_length=255, verbose_name='کلیدواژه')
#     content = models.CharField(max_length=255, verbose_name='محتوا')

#     class Meta:
#         verbose_name = 'متا تگ'
#         verbose_name_plural = 'متا تگ‌ها'

#     def __str__(self):
#         return self.keyword


class Province(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام استان')
    country = models.CharField(max_length=255, default='ایران', verbose_name='کشور')
    countrycode = models.IntegerField(default=98, verbose_name='کد کشور')
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='latitude')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='longitude')
    image = models.ImageField(upload_to='images/core/province/', default='images/core/province/default.png', 
                              validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])],
                              blank=True, null=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان‌ها'

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='شناسه استان')
    name = models.CharField(max_length=255, verbose_name='نام شهر')
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='latitude')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='longitude')

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'

    def __str__(self):
        return self.name
    

# class Billboard(models.Model):
#     TYPE_SLIDER = 'slider'
#     TYPE_BANNER = 'banner'
#     TYPE_POSTER = 'poster'
#     TYPE_CHOICES = (
#         (TYPE_SLIDER, 'اسلایدر'),
#         (TYPE_BANNER, 'بنر'),
#         (TYPE_POSTER, 'پوستر')
#     )

#     POSITION_TOP = 'top'
#     POSITION_MID = 'middle'
#     POSITION_BOT = 'bottom'
#     POSITION_CHOICES = (
#         (POSITION_TOP, 'بالا'),
#         (POSITION_MID, 'میانه'),
#         (POSITION_BOT, 'پایین'),
#     )
#     STATUS_DRAFT = 'draft'
#     STATUS_PUBLISH = 'publish'
#     STATUS_INVISIBLE = 'invisible'
#     STATUS_CHOICES = (
#         (STATUS_DRAFT, 'در صف انتشار'),
#         (STATUS_PUBLISH, 'منتشر شده'),
#         (STATUS_INVISIBLE, 'پنهان شده'),
#     )

#     link = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینک')
#     caption = models.CharField(max_length=255, blank=True, null=True, verbose_name='کپشن')
#     image_desktop = models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (دسکتاپ)')
#     image_tablet = models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (تبلت)')
#     image_mobile = models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (موبایل)')
#     alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیحات تصویر')
#     type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع')
#     position = models.CharField(max_length=255, choices=POSITION_CHOICES, default=POSITION_TOP, verbose_name='موقعیت')
#     status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_DRAFT, verbose_name='وضعیت')

#     class Meta:
#         verbose_name = 'بیلبورد'
#         verbose_name_plural = 'بیلبوردها'

#     def __str__(self):
#         return self.link


# class Faq(models.Model):
#     SUBJECT_PURCHASE = 'purchase'
#     SUBJECT_COURIER = 'courier'
#     SUBJECT_REGISTRATION = 'registration'
#     SUBJECT_CHOICES = (
#         (SUBJECT_PURCHASE, 'خرید'),
#         (SUBJECT_COURIER, 'ارسال مرسولات'),
#         (SUBJECT_REGISTRATION, 'ثبت نام'),
#     )

#     subject = models.CharField(max_length=255, choices=SUBJECT_CHOICES, verbose_name='موضوع')
#     order = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name='ترتیب نمایش')
#     question = models.CharField(max_length=255, verbose_name='سوال')
#     answer = models.TextField(verbose_name='پاسخ')

#     class Meta:
#         verbose_name = 'سوال متداول'
#         verbose_name_plural = 'سوالات متداول'

#     def __str__(self):
#         return f"{self.subject} - {self.question}"


# class ContactUs(models.Model):
#     full_name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
#     email = models.EmailField(max_length=255, blank=True, null=True, verbose_name="ایمیل")
#     phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="شماره تماس")
#     title = models.CharField(max_length=255, verbose_name="عنوان")
#     body = models.CharField(max_length=255, verbose_name="متن پیام")
#     status = models.BooleanField(default=False, verbose_name="وضعیت")
#     date = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت")

#     class Meta:
#         verbose_name = 'تماس با ما'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return f"{self.full_name} - {self.title}"
