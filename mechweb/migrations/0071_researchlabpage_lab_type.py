# Generated by Django 2.2.1 on 2019-06-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0070_publicationpagegalleryimage_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchlabpage',
            name='lab_type',
            field=models.CharField(choices=[('0', 'UG'), ('1', 'PG')], default='0', max_length=2),
        ),
    ]
