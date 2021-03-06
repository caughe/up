# Generated by Django 3.1.2 on 2020-10-08 16:38

import creditcards.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_first_name', models.CharField(max_length=50)),
                ('cust_last_name', models.CharField(max_length=50)),
                ('cust_email', models.EmailField(max_length=100)),
                ('cust_id', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=50)),
                ('cust_bill_card', creditcards.models.CardNumberField(max_length=25, verbose_name='card number')),
                ('cust_bill_expiry', creditcards.models.CardExpiryField(verbose_name='expiration date')),
                ('cust_bill_code', creditcards.models.SecurityCodeField(max_length=4, verbose_name='security code')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
