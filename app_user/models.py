from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator 


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="شماره موبایل")
    avatar = models.ImageField(blank=True, null=True, verbose_name='لوگو', 
                               upload_to='images/account/user/', default="images/account/user/default.png",
                               validators=[FileExtensionValidator(['png'])])

    def __str__(self):
        return f'{self.get_username()} | {self.get_full_name()}'
    


