# Generated by Django 5.1.2 on 2024-10-30 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('vaccine', '0002_alter_vaccine_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('target_population', models.IntegerField()),
                ('status', models.CharField(choices=[('Planned', 'Planned'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=10)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=250)),
                ('dose_per_individual', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccine')),
            ],
        ),
    ]
