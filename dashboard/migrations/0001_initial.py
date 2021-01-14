# Generated by Django 3.1.5 on 2021-01-14 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VeterinaryOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=254)),
                ('county', models.CharField(max_length=100)),
                ('idNo', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Veterinary Officers',
                'db_table': 'Veterinary_Officers',
            },
        ),
    ]