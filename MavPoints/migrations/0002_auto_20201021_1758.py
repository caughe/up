# Generated by Django 3.1.2 on 2020-10-21 22:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MavPoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('employee', 'EMPLOYEE'), ('customer', 'CUSTOMER')], default='employee', max_length=50)),
                ('emp_first_name', models.CharField(max_length=50)),
                ('emp_last_name', models.CharField(max_length=50)),
                ('emp_email', models.EmailField(max_length=100)),
                ('emp_id', models.IntegerField()),
                ('phone_number', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cust_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='role',
            field=models.CharField(choices=[('employee', 'EMPLOYEE'), ('customer', 'CUSTOMER')], default='customer', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cust_email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
