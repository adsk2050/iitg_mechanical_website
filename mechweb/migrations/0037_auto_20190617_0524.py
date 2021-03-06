# Generated by Django 2.2.1 on 2019-06-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0036_aboutiitgmech'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnuspage',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='middle name'),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staffpage',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='studentpage',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='alumnuspage',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='alumnuspage',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
