# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinedTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('planned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to='login_app.User')),
                ('users_joined', models.ManyToManyField(related_name='joined_users', to='login_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='joinedtrip',
            name='trip_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels_app.Trip'),
        ),
    ]