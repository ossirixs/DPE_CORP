# Generated by Django 3.1.2 on 2021-03-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20210213_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcode',
            name='seconds_integrity',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='testcode',
            name='expiration',
            field=models.DateField(blank=True, null=True),
        ),
    ]
