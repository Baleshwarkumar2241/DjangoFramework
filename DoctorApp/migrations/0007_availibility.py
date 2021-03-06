# Generated by Django 2.1.7 on 2021-07-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorApp', '0006_auto_20210709_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilies', to='DoctorApp.Facility')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilies', to='DoctorApp.Hospital')),
            ],
        ),
    ]
