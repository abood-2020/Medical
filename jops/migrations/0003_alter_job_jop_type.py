# Generated by Django 3.2.7 on 2021-09-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jops', '0002_job_jop_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jop_type',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], default='FullTime', max_length=20),
        ),
    ]