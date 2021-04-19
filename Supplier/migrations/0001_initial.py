# Generated by Django 2.2.5 on 2019-09-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('Supplier_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Supplier_Name', models.CharField(max_length=50)),
                ('Supplier_Mailid', models.CharField(max_length=50)),
                ('Supplier_Mobile', models.IntegerField()),
                ('City', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['Supplier_Name'],
            },
        ),
    ]