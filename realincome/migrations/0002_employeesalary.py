# Generated by Django 4.0.2 on 2022-02-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realincome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_per_hour', models.IntegerField()),
                ('working_hour', models.IntegerField()),
                ('allowance', models.IntegerField()),
            ],
        ),
    ]
