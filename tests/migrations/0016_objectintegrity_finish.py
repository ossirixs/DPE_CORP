# Generated by Django 3.1.2 on 2021-04-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0015_maxpositions_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectintegrity',
            name='finish',
            field=models.BooleanField(default=False, help_text='if the applicant finished the test'),
        ),
    ]
