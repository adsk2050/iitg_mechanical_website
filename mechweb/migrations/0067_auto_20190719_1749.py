# Generated by Django 2.2.1 on 2019-07-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0066_auto_20190719_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepage',
            name='eligible_programmes',
            field=models.CharField(choices=[('0', 'Bachelor'), ('1', 'Masters'), ('2', 'Research Scholar'), ('3', 'Other')], default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='five',
            field=models.BooleanField(default=False, verbose_name='M.Tech: Machine Design'),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='five_sem',
            field=models.IntegerField(blank=True, default=1, verbose_name='Semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursepage',
            name='four',
            field=models.BooleanField(default=False, verbose_name='M.Tech: Fluids and Thermal'),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='four_sem',
            field=models.IntegerField(blank=True, default=1, verbose_name='Semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursepage',
            name='one',
            field=models.BooleanField(default=False, verbose_name='M.Tech: Aerodynamics & Propulsion '),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='one_sem',
            field=models.IntegerField(blank=True, default=1, verbose_name='Semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursepage',
            name='six',
            field=models.BooleanField(default=False, verbose_name='PhD'),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='six_sem',
            field=models.IntegerField(blank=True, default=1, verbose_name='Semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursepage',
            name='three',
            field=models.BooleanField(default=False, verbose_name='M.Tech: Computational Mechanics'),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='three_sem',
            field=models.IntegerField(blank=True, default=1, verbose_name='Semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursepage',
            name='two',
            field=models.BooleanField(default=False, verbose_name='M.Tech: Manufacturing Science and Engineering'),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='two_sem',
            field=models.IntegerField(blank=True, default=1, verbose_name='Semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursepage',
            name='zero',
            field=models.BooleanField(default=True, verbose_name='B. Tech'),
        ),
        migrations.AddField(
            model_name='coursepage',
            name='zero_sem',
            field=models.IntegerField(blank=True, default=1, verbose_name='Semester'),
            preserve_default=False,
        ),
    ]
