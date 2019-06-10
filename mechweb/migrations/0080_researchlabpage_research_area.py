# Generated by Django 2.2.1 on 2019-06-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0079_auto_20190609_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchlabpage',
            name='research_area',
            field=models.CharField(choices=[('0', 'Thermal and Fluid Engineering'), ('1', 'Machine Design Engineering'), ('2', 'Manufacturing Engineering')], default='0', max_length=2),
        ),
    ]