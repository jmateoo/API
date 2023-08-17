# Generated by Django 4.2.4 on 2023-08-13 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('department', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('job', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_id', to='api.department')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_id', to='api.job')),
            ],
        ),
    ]
