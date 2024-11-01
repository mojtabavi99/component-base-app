from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', blank=True, null=True, on_delete=models.CASCADE)
    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    url_name = models.SlugField(blank=True, max_length=255, allow_unicode=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    poster = models.ImageField(blank=True, null=True,
                               upload_to='images/blog/category/', default='images/blog/category/default.png')
    alt = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_fa


class ArticleTag(models.Model):
    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    url_name = models.SlugField(blank=True, max_length=255, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_fa


class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(ArticleTag)
    title = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, allow_unicode=True, db_index=True, unique=True)
    intro = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    poster = models.ImageField(blank=True, null=True,
                               upload_to='images/blog/article/', default="images/blog/article/default.png")
    video = models.FileField(blank=True, null=True,
                             upload_to='images/blog/article/')
    alt = models.CharField(max_length=255, blank=True, null=True)
    published = models.BooleanField(default=False)
    preview = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'مقالات'
        verbose_name = 'مقاله'

    @property
    def getCategory(self):
        return self.category.name_fa

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ArticleContent(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    order = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(30)])
    head = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    tip = models.CharField(max_length=255, blank=True, null=True)
    poster = models.ImageField(upload_to='images/blog/article-content/', blank=True, null=True)
    video = models.FileField(upload_to='videos/blog/article-content/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    alt = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.head


class ArticleMeta(models.Model):
    ARTICLE_META_TYPE = (
        ('rel', 'rel'),
        ('name', 'name'),
        ('property', 'property')
    )

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=ARTICLE_META_TYPE)
    keyword = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.keyword
