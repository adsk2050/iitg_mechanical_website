# Generated by Django 2.2.1 on 2019-06-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0056_studentpage_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentproject',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]