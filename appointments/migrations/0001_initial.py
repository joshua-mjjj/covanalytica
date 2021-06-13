# Generated by Django 3.1.5 on 2021-06-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('sickness', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('guardian', models.CharField(blank=True, max_length=100, null=True)),
                ('doctor', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=300)),
            ],
        ),
    ]