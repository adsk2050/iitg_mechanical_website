# Generated by Django 2.2.1 on 2019-07-19 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0062_auto_20190719_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursepage',
            name='eligible_programmes',
        ),
        migrations.RemoveField(
            model_name='coursepage',
            name='eligible_specializations',
        ),
    ]
