# Generated by Django 5.0.6 on 2024-07-01 13:54

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycloud', '0002_account_is_staff_alter_account_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='external_file_path',
            field=models.CharField(max_length=50, unique=True, verbose_name='Cсылка на файл'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file_path',
            field=models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='storage'), upload_to='', verbose_name='Путь к файлу'),
        ),
    ]
