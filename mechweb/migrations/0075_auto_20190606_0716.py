# Generated by Django 2.2.1 on 2019-06-06 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0074_auto_20190606_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnihomepage',
            options={'verbose_name': 'Alumni Home'},
        ),
        migrations.AlterModelOptions(
            name='alumnuspage',
            options={'verbose_name': 'Alumnus', 'verbose_name_plural': 'Alumni'},
        ),
        migrations.AlterModelOptions(
            name='coursepage',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='coursestructure',
            options={'verbose_name': 'Course Structure', 'verbose_name_plural': 'CourseStructure'},
        ),
        migrations.AlterModelOptions(
            name='eventhomepage',
            options={'verbose_name': 'Event Home'},
        ),
        migrations.AlterModelOptions(
            name='eventpage',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='facultypage',
            options={'verbose_name': 'Faculty', 'verbose_name_plural': 'Faculty'},
        ),
        migrations.AlterModelOptions(
            name='mechhomepage',
            options={'verbose_name': 'Home'},
        ),
        migrations.AlterModelOptions(
            name='projecthomepage',
            options={'verbose_name': 'Project Home'},
        ),
        migrations.AlterModelOptions(
            name='projectpage',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='publicationhomepage',
            options={'verbose_name': 'Publication Home'},
        ),
        migrations.AlterModelOptions(
            name='publicationpage',
            options={'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
        migrations.AlterModelOptions(
            name='researchhomepage',
            options={'verbose_name': 'Research Home'},
        ),
        migrations.AlterModelOptions(
            name='researchlabpage',
            options={'verbose_name': 'Lab', 'verbose_name_plural': 'Labs'},
        ),
        migrations.AlterModelOptions(
            name='staffhomepage',
            options={'verbose_name': 'Staff Home'},
        ),
        migrations.AlterModelOptions(
            name='staffpage',
            options={'verbose_name': 'Staff', 'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterModelOptions(
            name='studenthomepage',
            options={'verbose_name': 'Student Home'},
        ),
        migrations.AlterModelOptions(
            name='studentpage',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
    ]