# Generated by Django 3.0.5 on 2020-05-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset', '0002_auto_20200528_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='Accessories',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Location_Name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Location_Number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
