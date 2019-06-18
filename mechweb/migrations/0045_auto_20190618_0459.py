# Generated by Django 2.2.1 on 2019-06-18 04:59

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0044_auto_20190618_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='interestcategories',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='interestcategories',
            name='category',
            field=models.CharField(choices=[('0', 'Other'), ('1', 'Machine Design Engineering'), ('2', 'Manufacturing Engineering'), ('3', 'Thermal and Fluid Engineering')], default='0', max_length=2, unique=True),
        ),
    ]
