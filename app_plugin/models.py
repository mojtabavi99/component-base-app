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


class Meta(models.Model):
    META_TYPE = (
        ('rel', 'rel'),
        ('name', 'name'),
        ('property', 'property')
    )

    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    type = models.CharField(max_length=255, choices=META_TYPE, verbose_name='نوع تگ')
    keyword = models.CharField(max_length=255, verbose_name='کلیدواژه')
    content = models.CharField(max_length=255, verbose_name='محتوا')

    class Meta:
        verbose_name = 'متا تگ'
        verbose_name_plural = 'متا تگ‌ها'

    def __str__(self):
        return self.keyword


class Text(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    head = models.CharField(max_length=255, blank=True, null=True, verbose_name='عنوات')
    body = models.TextField(verbose_name='متن')
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return self.head


class Faq(models.Model):
    SUBJECT_PURCHASE = 'purchase'
    SUBJECT_COURIER = 'courier'
    SUBJECT_REGISTRATION = 'registration'
    SUBJECT_CHOICES = (
        (SUBJECT_PURCHASE, 'خرید'),
        (SUBJECT_COURIER, 'ارسال مرسولات'),
        (SUBJECT_REGISTRATION, 'ثبت نام'),
    )

    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    subject = models.CharField(max_length=255, choices=SUBJECT_CHOICES, verbose_name='موضوع')
    order = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name='ترتیب نمایش')
    question = models.CharField(max_length=255, verbose_name='سوال')
    answer = models.TextField(verbose_name='پاسخ')

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'

    def __str__(self):
        return f'{self.subject} - {self.question}'


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

    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='شناسه صفحه')
    model = models.CharField(max_length=255, choices=MODEL_CHOICES, verbose_name='مدل')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع کاتالوگ')
    name = models.CharField(max_length=255, verbose_name='نام کاتالوگ')
    see_all_link = models.CharField(max_length=255, blank=True, null=True, verbose_name='لینک موارد بیشتر')
    with_background = models.BooleanField(default=False, verbose_name='پس‌زمینه دارد؟')
    background_color = models.CharField(max_length=255, blank=True, null=True, verbose_name='رنگ پس‌زمینه')
    with_header = models.BooleanField(default=False, verbose_name='سربرگ دارد؟')
    header_image_desktop = models.ImageField(upload_to='images/plugin/list/', default='images/plugin/list/default.png', 
                                             validators=[FileExtensionValidator(['png, jpg, jpeg, webp, svg'])], 
                                             blank=True, null=True, verbose_name='تصویر سربرگ (دسکتاپ)')
    header_image_mobile = models.ImageField(upload_to='images/plugin/list/', default='images/plugin/list/default.png', 
                                            validators=[FileExtensionValidator(['png, jpg, jpeg, webp, svg'])], 
                                            blank=True, null=True, verbose_name='تصویر سربرگ (موبایل)')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیحات تصویر')

    class Meta:
        verbose_name = 'کاتالوگ'
        verbose_name_plural = 'لیست کاتالوگ‌ها'

    def __str__(self):
        return self.name


class CatalogSet(models.Model):
    GENERATED_AUTO = 'auto'
    GENERATED_MANUAL = 'manual'
    GENERATED_CHOICES = (
        (GENERATED_AUTO, 'خودکار'),
        (GENERATED_MANUAL, 'دستی'),
    )

    generated = models.CharField(max_length=255, choices=GENERATED_CHOICES, verbose_name='روش تولید')
    name = models.CharField(max_length=255, verbose_name='نام گروه')
    max_items = models.IntegerField(default=0, verbose_name='حداکثر تعداد')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')

    class Meta:
        verbose_name = 'مجموعه‌ی کاتالوگ'
        verbose_name_plural = 'مجموعه‌های کاتالوگ'

    def __str__(self):
        return self.name
    

class CatalogSetItem(models.Model):
    set = models.ForeignKey(CatalogSet, on_delete=models.CASCADE, verbose_name='شناسه مجموعه')
    item = models.IntegerField(verbose_name='شناسه مورد')

    class Meta:
        verbose_name = 'اجزا کاتالوگ'
        verbose_name_plural = 'لیست اجزا کاتالوگ'

    def __str__(self):
        return f'{self.set.name} - {self.item}'


class CatalogContent(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='')
    set = models.F


class Breadcrumb(models.Model):
    pass

