# Generated by Django 3.1.1 on 2020-12-30 16:39

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0127_auto_20201230_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='programspecialization',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]