# Generated by Django 3.1.2 on 2021-03-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0140_auto_20210313_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email_id',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Personal Email ID'),
        ),
    ]