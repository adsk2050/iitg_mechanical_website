# Generated by Django 2.2.1 on 2020-02-10 15:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0093_auto_20200210_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='about',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='history',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='vision',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='alumnuspage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 9, 15, 43, 42, 318017, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='tenure_end',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 15, 43, 42, 339763, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 9, 15, 43, 42, 318017, tzinfo=utc)),
        ),
    ]