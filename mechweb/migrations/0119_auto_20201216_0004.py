# Generated by Django 3.1.1 on 2020-12-15 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0118_auto_20201216_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='effectivetimeperiod',
            old_name='end_time',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='effectivetimeperiod',
            old_name='start_time',
            new_name='start',
        ),
    ]