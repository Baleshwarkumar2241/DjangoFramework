# Generated by Django 2.1.7 on 2021-07-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorApp', '0004_auto_20210708_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
