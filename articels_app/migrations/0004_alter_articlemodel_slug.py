# Generated by Django 5.1.7 on 2025-06-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articels_app', '0003_alter_articlemodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, verbose_name='عنوان در مرورگر'),
        ),
    ]
