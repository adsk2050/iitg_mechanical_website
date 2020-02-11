# Generated by Django 2.2.1 on 2020-02-11 18:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0099_auto_20200211_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnuspage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 10, 18, 38, 47, 328106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='tenure_end',
            field=models.DateField(default=datetime.datetime(2021, 2, 10, 18, 38, 47, 351687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 10, 18, 38, 47, 328106, tzinfo=utc)),
        ),
    ]