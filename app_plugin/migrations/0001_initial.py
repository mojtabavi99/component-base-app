# Generated by Django 5.1.4 on 2024-12-30 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک')),
                ('caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='کپشن')),
                ('image_desktop', models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (دسکتاپ)')),
                ('image_tablet', models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (تبلت)')),
                ('image_mobile', models.ImageField(upload_to='images/core/slider/', verbose_name='تصویر (موبایل)')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='توضیحات تصویر')),
                ('type', models.CharField(choices=[('slider', 'اسلایدر'), ('banner', 'بنر'), ('poster', 'پوستر')], max_length=255, verbose_name='نوع')),
                ('position', models.CharField(choices=[('top', 'بالا'), ('middle', 'میانه'), ('bottom', 'پایین')], default='top', max_length=255, verbose_name='موقعیت')),
                ('status', models.CharField(choices=[('draft', 'در صف انتشار'), ('publish', 'منتشر شده'), ('invisible', 'پنهان شده')], default='draft', max_length=255, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'بیلبورد',
                'verbose_name_plural': 'بیلبوردها',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('purchase', 'خرید'), ('courier', 'ارسال مرسولات'), ('registration', 'ثبت نام')], max_length=255, verbose_name='موضوع')),
                ('order', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='ترتیب نمایش')),
                ('question', models.CharField(max_length=255, verbose_name='سوال')),
                ('answer', models.TextField(verbose_name='پاسخ')),
            ],
            options={
                'verbose_name': 'سوال متداول',
                'verbose_name_plural': 'سوالات متداول',
            },
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('rel', 'rel'), ('name', 'name'), ('property', 'property')], max_length=255, verbose_name='نوع تگ')),
                ('keyword', models.CharField(max_length=255, verbose_name='کلیدواژه')),
                ('content', models.CharField(max_length=255, verbose_name='محتوا')),
            ],
            options={
                'verbose_name': 'متا تگ',
                'verbose_name_plural': 'متا تگ\u200cها',
            },
        ),
    ]