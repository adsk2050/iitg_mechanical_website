# Generated by Django 2.2.1 on 2019-06-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0061_auto_20190604_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='labequipment',
            name='funding_agency',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='labequipment',
            name='funding_agency_link',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]