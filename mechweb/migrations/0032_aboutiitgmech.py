# Generated by Django 2.2.1 on 2019-06-16 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
        ('mechweb', '0031_labequipment_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutiitgmech',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('vision', models.CharField(blank=True, max_length=500)),
                ('History', models.CharField(blank=True, max_length=500)),
                ('About', models.CharField(blank=True, max_length=500)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
