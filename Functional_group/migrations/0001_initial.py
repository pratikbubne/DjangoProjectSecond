# Generated by Django 2.2.5 on 2019-09-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalGroup',
            fields=[
                ('Fun_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Functional_Group', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['Functional_Group'],
            },
        ),
    ]
