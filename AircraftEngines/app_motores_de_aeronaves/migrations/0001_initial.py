# Generated by Django 4.2.7 on 2023-11-29 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='atmos',
            fields=[
                ('alt', models.FloatField(primary_key=True, serialize=False)),
                ('T0', models.FloatField(default=288.15)),
                ('P0', models.FloatField(default=101325.0)),
                ('rho0', models.FloatField(default=1.22)),
                ('a0', models.FloatField(default=340.2939)),
            ],
        ),
        migrations.CreateModel(
            name='motor',
            fields=[
                ('name', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('motor_type', models.TextField(max_length=20)),
                ('on_design', models.BooleanField()),
                ('ideal', models.BooleanField()),
                ('choked', models.BooleanField()),
                ('M0', models.FloatField()),
                ('hpr', models.FloatField()),
                ('cp_c', models.FloatField()),
                ('cp_t', models.FloatField()),
                ('gamma_c', models.FloatField()),
                ('gamma_t', models.FloatField()),
                ('Tt4', models.FloatField()),
                ('speed_in_combustion', models.FloatField()),
                ('lenght', models.FloatField()),
                ('d0', models.FloatField()),
                ('d1', models.FloatField()),
                ('d2', models.FloatField()),
                ('d3', models.FloatField()),
                ('d4', models.FloatField()),
                ('d5', models.FloatField()),
                ('d6', models.FloatField()),
                ('d7', models.FloatField()),
                ('d8', models.FloatField()),
                ('d9', models.FloatField()),
            ],
        ),
    ]
