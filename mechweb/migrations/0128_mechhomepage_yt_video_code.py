# Generated by Django 3.1.2 on 2021-03-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0127_academics_course_courseannouncement_coursefaculty_customsupervisor_effectivetimeperiod_program_progr'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechhomepage',
            name='yt_video_code',
            field=models.CharField(blank=True, max_length=264, null=True, verbose_name='Youtube video code'),
        ),
    ]