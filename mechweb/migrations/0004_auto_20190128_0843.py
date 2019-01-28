# Generated by Django 2.1.5 on 2019-01-28 08:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0003_mechhomepagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometextpanel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mechhomepagegalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='mechweb.MechHomePage'),
        ),
    ]
