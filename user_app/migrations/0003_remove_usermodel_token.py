# Generated by Django 5.1.7 on 2025-06-15 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_usermodel_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='token',
        ),
    ]
