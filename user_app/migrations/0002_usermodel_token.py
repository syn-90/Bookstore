# Generated by Django 5.1.7 on 2025-04-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='token',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
