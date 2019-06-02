# Generated by Django 2.2.1 on 2019-06-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0038_facultypage_additional_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultypage',
            name='disciplinary_committee',
            field=models.CharField(choices=[('Not_Applicable', 'Not_Applicable'), ('Chairman', 'Chairman'), ('Secretary', 'Secretary'), ('Member_Secretary', 'Member_Secretary'), ('Student_Member', 'Student_Member')], default='Not_Applicable', max_length=25),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='disposal_committee',
            field=models.CharField(choices=[('Not_Applicable', 'Not_Applicable'), ('Chairman', 'Chairman'), ('Member', 'Member'), ('External_Member', 'External_Member'), ('Non_Member_Secretary', 'Non_Member_Secretary')], default='Not_Applicable', max_length=25),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='dppc',
            field=models.CharField(choices=[('Not_Applicable', 'Not_Applicable'), ('Chairman', 'Chairman'), ('Secretary', 'Secretary'), ('Faculty_Member', 'Faculty_Member'), ('External_Member', 'External_Member'), ('PhD_Student_Member', 'PhD_Student_Member'), ('MTech_Student_Member', 'MTech_Student_Member')], default='Not_Applicable', max_length=25),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='dupc',
            field=models.CharField(choices=[('Not_Applicable', 'Not_Applicable'), ('Chairman', 'Chairman'), ('Secretary', 'Secretary'), ('Faculty_Member', 'Faculty_Member'), ('External_Member', 'External_Member'), ('3rd_year_BTech', '3rd_year_BTech'), ('2nd_year_BTech', '2nd_year_BTech')], default='Not_Applicable', max_length=25),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='faculty_in_charge',
            field=models.CharField(choices=[('Not_Applicable', 'Not_Applicable'), ('BTP_Co_ordinator', 'BTP_Co_ordinator'), ('MTP_Co_ordinator', 'MTP_Co_ordinator'), ('Central_Workshop', 'Central_Workshop'), ('Library_Committee', 'Library_Committee'), ('Training_and_Placement', 'Training_and_Placement'), ('Departmental_Seminar_Room', 'Departmental_Seminar_Room'), ('Secretary_Faculty_Meeting', 'Secretary_Faculty_Meeting'), ('PG_Computational_Lab', 'PG_Computational_Lab'), ('Research_Scholar_Room', 'Research_Scholar_Room'), ('Time_Table_Committee', 'Time_Table_Committee'), ('Departmental_Website', 'Departmental_Website')], default='Not_Applicable', max_length=25),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='laboratory_in_charge',
            field=models.CharField(choices=[('Not_Applicable', 'Not_Applicable'), ('Advanced_Manufacturing_Laboratory', 'Advanced_Manufacturing_Laboratory'), ('CAD_Laboratory', 'CAD_Laboratory'), ('Central_Workshop', 'Central_Workshop'), ('Fluid_Mechanics_Laboratory', 'Fluid_Mechanics_Laboratory'), ('IC_Engines_Laboratory', 'IC_Engines_Laboratory'), ('Instrumentation_and_Control_Laboratory', 'Instrumentation_and_Control_Laboratory'), ('Material_Science_Laboratory', 'Material_Science_Laboratory'), ('Tribology_Laboratory', 'Tribology_Laboratory'), ('Mechatronics_and_Robotics_Laboratory', 'Mechatronics_and_Robotics_Laboratory'), ('Strength_of_Materials_Laboratory', 'Strength_of_Materials_Laboratory'), ('Theory_of_Machines_Laboratory', 'Theory_of_Machines_Laboratory'), ('Thermal_Science_Laboratory', 'Thermal_Science_Laboratory'), ('Turbo_Machinary_Laboratory', 'Turbo_Machinary_Laboratory'), ('Vibrations_and_Acoustics_Laboratory', 'Vibrations_and_Acoustics_Laboratory')], default='Not_Applicable', max_length=25),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='additional_roles',
            field=models.CharField(choices=[('Not_Applicable', 'Not_Applicable'), ('HoD', 'HoD'), ('Director', 'Director')], default='Not_Applicable', max_length=25),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='designation',
            field=models.CharField(choices=[('HAG', 'HAG'), ('Professor', 'Professor'), ('Assistant_Professor', 'Assistant_Professor'), ('Associate_Professor', 'Associate_Professor'), ('Visiting_Professor', 'Visiting_Professor'), ('Professor_On_lien', 'Professor_On_lien')], default='Assistant_Professor', max_length=25),
        ),
    ]