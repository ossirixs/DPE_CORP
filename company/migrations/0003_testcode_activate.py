# Generated by Django 3.1.2 on 2020-12-22 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_testcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcode',
            name='activate',
            field=models.BooleanField(default=True),
        ),
    ]