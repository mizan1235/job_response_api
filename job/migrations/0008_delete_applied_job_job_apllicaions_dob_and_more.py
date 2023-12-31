# Generated by Django 4.2.3 on 2023-12-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_apllicaions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='applied_job',
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='DOB',
            field=models.DateField(default='17/09/2003', max_length=15),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='address',
            field=models.CharField(default='Your Default Address', max_length=150),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='email',
            field=models.EmailField(default='rahul@gamil.com', max_length=30),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='experience',
            field=models.CharField(default='rahul', max_length=300),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='father_name',
            field=models.CharField(default='rahul', max_length=40),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='hometown',
            field=models.CharField(default='new work', max_length=20),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='mother_name',
            field=models.CharField(default='rahul', max_length=40),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='name',
            field=models.CharField(default='rahul', max_length=50),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='pin',
            field=models.IntegerField(default='781316'),
        ),
        migrations.AddField(
            model_name='job_apllicaions',
            name='resume',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='resume/'),
        ),
        migrations.AlterField(
            model_name='job_apllicaions',
            name='job_id',
            field=models.IntegerField(default='3'),
        ),
        migrations.AlterField(
            model_name='job_apllicaions',
            name='username',
            field=models.CharField(default='rahul123', max_length=40),
        ),
    ]
