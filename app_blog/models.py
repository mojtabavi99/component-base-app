from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, 
                               blank=True, null=True, verbose_name='شناسه والد')
    name_fa = models.CharField(max_length=255, verbose_name='نام دسته (فارسی)')
    name_en = models.CharField(max_length=255, verbose_name='نام دسته (انگلیسی)')
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True, verbose_name='slug')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    poster = models.ImageField(upload_to='images/blog/category/', default='images/blog/category/default.png', 
                               validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])], 
                               blank=True, null=True, verbose_name='پوستر')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='متن جایگزین عکس')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی مقالات'

    @property
    def getArticlesCount(self):
        return Article.objects.filter(category=self).count()

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name_fa, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_fa


class ArticleTag(models.Model):
    name_fa = models.CharField(max_length=255, verbose_name='نام برچسب (فارسی)')
    name_en = models.CharField(max_length=255, verbose_name='نام برچسب (انگلیسی)')
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True, verbose_name='slug')

    class Meta:
        verbose_name = 'برچب'
        verbose_name_plural = 'برچسب‌های مقالات'

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name_fa, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_fa


class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING, verbose_name='دسته بندی مقالات‌')
    tag = models.ManyToManyField(ArticleTag, verbose_name='برچسب ها')
    title = models.CharField(max_length=255, verbose_name='عنوان مقاله')
    page_title = models.CharField(max_length=255, verbose_name='عنوان صفحه')
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True, verbose_name='slug')
    intro = models.TextField(verbose_name='مقدمه')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    poster = models.ImageField(upload_to='images/blog/article/', default='images/blog/article/default.png', 
                               validators=[FileExtensionValidator(['png, jpg, jpeg, webp'])], 
                               blank=True, null=True, verbose_name='پوستر')
    video = models.FileField(upload_to='videos/blog/article/', blank=True, null=True, verbose_name='ویدیو')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='متن جایگزین عکس')
    published = models.BooleanField(default=False, verbose_name='وضعیت انتشار')
    preview = models.BooleanField(default=False, verbose_name='نمایش / عدم نمایش')

    class Meta:
        verbose_name_plural = 'مقالات'
        verbose_name = 'مقاله'

    @property
    def getCategory(self):
        return self.category.name_fa

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    


