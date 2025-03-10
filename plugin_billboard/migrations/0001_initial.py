# Generated by Django 5.1.4 on 2025-02-23 16:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_core', '0003_page_province_alt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('type', models.CharField(choices=[('slider', 'اسلایدر'), ('banner', 'بنر'), ('poster', 'پوستر')], max_length=255, verbose_name='نوع')),
                ('status', models.CharField(choices=[('draft', 'در صف انتشار'), ('publish', 'منتشر شده'), ('invisible', 'پنهان شده')], default='draft', max_length=255, verbose_name='وضعیت')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.page', verbose_name='شناسه صفحه')),
            ],
            options={
                'verbose_name': 'بیلبورد',
                'verbose_name_plural': 'بیلبوردها',
            },
        ),
        migrations.CreateModel(
            name='BillboardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک')),
                ('caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='کپشن')),
                ('image_desktop', models.ImageField(upload_to='images/plugin/billboard/', validators=[django.core.validators.FileExtensionValidator(['png, jpg, jpeg, webp'])], verbose_name='تصویر (دسکتاپ)')),
                ('image_mobile', models.ImageField(upload_to='images/plugin/billboard/', validators=[django.core.validators.FileExtensionValidator(['png, jpg, jpeg, webp'])], verbose_name='تصویر (موبایل)')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='متن جایگزین عکس')),
                ('Billboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plugin_billboard.billboard', verbose_name='شناسه بیلبورد')),
            ],
            options={
                'verbose_name': 'تصویر بیلبورد',
                'verbose_name_plural': 'تصاویر بیلبورد',
            },
        ),
    ]
