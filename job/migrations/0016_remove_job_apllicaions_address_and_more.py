# Generated by Django 4.2.3 on 2023-12-16 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_job_apllicaions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='address',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='email',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='hometown',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='name',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='job_apllicaions',
            name='resume',
        ),
    ]
