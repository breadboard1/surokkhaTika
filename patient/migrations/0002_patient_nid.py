# Generated by Django 5.1.2 on 2024-10-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nid',
            field=models.CharField(default=0, max_length=30, unique=True),
        ),
    ]
