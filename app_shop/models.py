from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator


class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, 
                               blank=True, null=True, verbose_name='شناسه والد')
    name_fa = models.CharField(max_length=255, verbose_name='نام دسته (فارسی)')
    name_en = models.CharField(max_length=255, verbose_name='نام دسته (انگلیسی)')
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True, verbose_name='slug')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    poster = models.ImageField(upload_to='images/shop/category/', default='images/shop/category/default.png', 
                               validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])], 
                               blank=True, null=True, verbose_name='پوستر')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='متن جایگزین عکس')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی محصولات'

    @property
    def getProductCount(self):
        return Product.objects.filter(category=self).count()

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name_fa, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_fa


class ProductTag(models.Model):
    name_fa = models.CharField(max_length=255, verbose_name='نام برچسب (فارسی)')
    name_en = models.CharField(max_length=255, verbose_name='نام برچسب (انگلیسی)')
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True, verbose_name='slug')

    class Meta:
        verbose_name = 'برچب'
        verbose_name_plural = 'برچسب‌های محصولات'

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name_fa, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_fa
    

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, verbose_name='دسته بندی محصولات')
    tag = models.ManyToManyField(ProductTag, verbose_name='برچسب ها', related_name='product_tags')
    name_fa = models.CharField(max_length=255, verbose_name='نام محصول (فارسی)')
    name_en = models.CharField(max_length=255, blank=True, null=True, verbose_name='نام محصول (انگلیسی)')
    page_title = models.CharField(max_length=255, verbose_name='عنوان محصول')
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True, verbose_name='slug')
    intro = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیحات مختصر')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    price = models.BigIntegerField(verbose_name='قیمت')
    discount = models.IntegerField(default=0, verbose_name='تخفیف')
    sales = models.IntegerField(default=0, verbose_name='تعداد فروش')
    in_stock = models.IntegerField(verbose_name='موجودیت')
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, verbose_name='امتیاز')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    poster = models.ImageField(upload_to='images/shop/product/', default='images/shop/product/default.png', 
                               validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])], 
                               blank=True, null=True, verbose_name='پوستر')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='متن جایگزین عکس')
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'لیست محصولات'

    @property
    def getCategory(self):
        return self.category.name_fa

    @property
    def discountedPrice(self):
        return (self.price * self.discount) / 100

    @property
    def sellPrice(self):
        return int(self.price - self.discountedPrice)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_fa, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_fa


class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='شناسه محصول')
    order = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(30)],
                                verbose_name='ترتیب نمایش')
    property = models.CharField(max_length=255, verbose_name='ویژگی')
    content = models.CharField(max_length=255, verbose_name='محتوا')

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی‌های محصول'

    def __str__(self):
        return self.property + ": " + self.content
    

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='شناسه محصول')
    image = models.ImageField(upload_to='images/shop/product/gallery/', verbose_name='عکس', 
                              validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])])

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'گالری محصولات'

    def __str__(self):
        return f'{self.product.name_fa}'
