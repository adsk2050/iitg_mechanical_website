# Generated by Django 2.1.5 on 2019-01-29 14:24

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0008_remove_eventpage_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_page', to='mechweb.EventHomePage'),
        ),
    ]
