# Generated by Django 2.1.5 on 2019-01-30 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('mechweb', '0013_auto_20190130_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='poster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
