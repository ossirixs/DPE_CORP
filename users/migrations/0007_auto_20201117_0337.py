# Generated by Django 3.1.2 on 2020-11-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201117_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.IntegerField(blank=True, verbose_name='Company'),
        ),
    ]