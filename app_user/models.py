import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator 

from app_core.models import Province, City
from utilities.tools import Gadgets

class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="شماره موبایل")
    avatar = models.ImageField(blank=True, null=True, verbose_name='عکس پروفایل', 
                               upload_to='images/account/user/', default="images/account/user/default.png",
                               validators=[FileExtensionValidator(['png'])])

    def __str__(self):
        return f'{self.get_username()} | {self.get_full_name()}'


class VerifyToken(models.Model):
    TYPE_EMAIL = 'email'
    TYPE_MOBILE = 'mobile'
    TYPE_CHOICES = (
        (TYPE_EMAIL, 'Email'),
        (TYPE_MOBILE, 'Mobile'),
    )

    type = models.CharField(max_length=255, default=TYPE_MOBILE, choices=TYPE_CHOICES, verbose_name="نوع")
    dest = models.CharField(max_length=255, verbose_name="ایمیل / موبایل")
    token = models.CharField(max_length=255, verbose_name="کد")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت")
    expires = models.DateTimeField(verbose_name="زمان انقضا")

    class Meta:
        verbose_name = 'کد فعالسازی'
        verbose_name_plural = 'کدهای فعالسازی'

    @staticmethod
    def generateCode(mode, dest):
        if mode == VerifyToken.TYPE_MOBILE:
            VerifyToken.objects.create(
                type=VerifyToken.TYPE_MOBILE,
                dest=dest,
                token=Gadgets.GenerateMobileToken(),
                expires=datetime.datetime.now() + datetime.timedelta(hours=0, minutes=2, seconds=30)
            )
        else:
            VerifyToken.objects.create(
                type=VerifyToken.TYPE_EMAIL,
                dest=dest,
                token=Gadgets.GenerateEmailToken(),
                expires=datetime.datetime.now() + datetime.timedelta(hours=0, minutes=2, seconds=30)
            )

    @staticmethod
    def codeValidation(dest, token):
        sample = VerifyToken.objects.filter(dest=dest, token=token)
        if sample.exists():
            VerifyToken.objects.filter(dest=dest).delete()
            return True
        else:
            return False

    def __str__(self):
        return f'{self.dest} - {self.token}'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='شناسه کاربر')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='شناسه استان')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='شناسه شهر')
    district = models.CharField(max_length=255, verbose_name='محله')
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='latitude')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, verbose_name='longitude')
    zip = models.CharField(max_length=50, verbose_name='کد پستی')
    tag = models.CharField(max_length=50, blank=True, null=True, verbose_name='پلاک')
    unit = models.CharField(max_length=50, blank=True, null=True, verbose_name='واحد')

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس‌ها'

    def __str__(self):
        return f"{self.province.name} - {self.city.name} - {self.district}"
