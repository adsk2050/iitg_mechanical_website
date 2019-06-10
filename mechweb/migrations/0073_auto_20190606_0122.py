# Generated by Django 2.2.1 on 2019-06-06 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0072_auto_20190605_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursestructure',
            name='nav_order',
            field=models.CharField(default=4, max_length=1),
        ),
        migrations.AddField(
            model_name='eventhomepage',
            name='nav_order',
            field=models.CharField(default=5, max_length=1),
        ),
        migrations.AddField(
            model_name='facultyhomepage',
            name='nav_order',
            field=models.CharField(default=2, max_length=1),
        ),
        migrations.AddField(
            model_name='researchhomepage',
            name='nav_order',
            field=models.CharField(default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='staffhomepage',
            name='nav_order',
            field=models.CharField(default=7, max_length=1),
        ),
        migrations.AddField(
            model_name='studenthomepage',
            name='nav_order',
            field=models.CharField(default=3, max_length=1),
        ),
    ]