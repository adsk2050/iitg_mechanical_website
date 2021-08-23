# Generated by Django 3.1.2 on 2021-07-30 18:57

import django.core.validators
from django.db import migrations, models
import mechweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0134_auto_20210704_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='thesis_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='studentbatch',
            name='graduation_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1994), mechweb.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrollment_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='leaving_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='webmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='studentbatch',
            name='enrollment_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1994), mechweb.models.max_value_current_year]),
        ),
    ]