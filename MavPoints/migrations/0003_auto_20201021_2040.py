# Generated by Django 3.1.2 on 2020-10-22 01:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MavPoints', '0002_auto_20201021_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='cust_email',
            field=models.EmailField(max_length=100),
        ),
    ]
