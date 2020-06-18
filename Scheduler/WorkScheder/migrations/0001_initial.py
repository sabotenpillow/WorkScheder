# Generated by Django 3.0.4 on 2020-05-29 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True, verbose_name='date')),
                ('work_schedule', models.CharField(max_length=5, verbose_name='work sched')),
            ],
            options={
                'verbose_name_plural': 'Workschedule',
            },
        ),
    ]
