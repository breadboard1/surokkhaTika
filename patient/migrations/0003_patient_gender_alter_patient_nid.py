# Generated by Django 5.1.2 on 2024-10-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_nid'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='male', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nid',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
