# Generated by Django 3.1.2 on 2020-11-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.CharField(choices=[('MAIN', 'Main'), ('BRANCH', 'Branch')], default='BRANCH', max_length=10),
        ),
    ]
