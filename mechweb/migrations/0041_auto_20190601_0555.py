# Generated by Django 2.2.1 on 2019-06-01 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0040_auto_20190601_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultypage',
            name='home_address_line_2',
        ),
        migrations.RemoveField(
            model_name='facultypage',
            name='home_address_line_3',
        ),
    ]