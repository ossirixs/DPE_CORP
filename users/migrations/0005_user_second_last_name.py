# Generated by Django 3.1.2 on 2020-11-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201027_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='second_last_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Name of user'),
        ),
    ]