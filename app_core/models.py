from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator


class Page(models.Model):
    MODEL_MAIN = 'main'
    MODEL_LANDING = 'landing'
    MODEL_ARTICLE = 'article'
    MODEL_PRODUCT = 'product'
    MODEL_CHOICES = (
        (MODEL_MAIN, 'اصلی'),
        (MODEL_LANDING, 'لندینگ'),
        (MODEL_ARTICLE, 'مقالات'),
        (MODEL_PRODUCT, 'محصولات'),
    )

    name = models.CharField(max_length=255, unique=True, verbose_name='نام صفحه')
    model = models.CharField(max_length=255, choices=MODEL_CHOICES, verbose_name='مدل')
    parent = models.IntegerField(default=0, verbose_name='شناسه والد')
    url = models.CharField(max_length=255, blank=True, null=True, unique=True, verbose_name='url')
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    
    class Meta:
        verbose_name = 'صفحه فرود'
        verbose_name_plural = 'صفحات فرود'

    def __str__(self):
        return self.name


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
    

class Province(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام استان')
    country = models.CharField(max_length=255, default='ایران', verbose_name='کشور')
    countrycode = models.IntegerField(default=98, verbose_name='کد کشور')
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True, verbose_name='slug')
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='latitude')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='longitude')
    image = models.ImageField(upload_to='images/core/province/', default='images/core/province/default.png', 
                              validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])],
                              blank=True, null=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان‌ها'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

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
    

# class PageComponent(models.Model):
#     page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="شناسه صفحه")
#     name = models.CharField()
#     order = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name='ترتیب نمایش')
#     type = models.CharField()
#     style = models.CharField()

#     def __str__(self):
#         return self.name


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
