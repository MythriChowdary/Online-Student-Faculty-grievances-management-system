# Generated by Django 4.2.5 on 2023-09-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_course_academicyear_alter_course_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('CSE(R)', 'CSE(Regular)'), ('CSE(H)', 'CSE(Honors)'), ('CSIT', 'CSIT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(choices=[('Prof', 'Professor'), ('Assoc.Prof', 'Associate Professor'), ('Asst.Prof', 'Assistant Professor')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(choices=[('M.TECH', 'M.TECH'), ('PH.D', 'PH.D')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('CSE(R)', 'CSE(Regular)'), ('CSE(H)', 'CSE(Honors)'), ('CSIT', 'CSIT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.CharField(choices=[('B.TECH', 'B.TECH'), ('M.TECH', 'M.TECH')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10),
        ),
    ]