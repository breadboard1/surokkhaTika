# Generated by Django 5.1.2 on 2024-10-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_patient_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
