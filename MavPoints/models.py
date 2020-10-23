from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.
Roles = (
    ('employee', 'EMPLOYEE'),
    ('customer', 'CUSTOMER'),
)

class Customer(AbstractBaseUser):
    object = UserManager()

    role = models.CharField(max_length=50, choices=Roles, default='customer')
    username = models.CharField(max_length=50, unique=True)
    cust_first_name = models.CharField(max_length=50)
    cust_last_name = models.CharField(max_length=50)
    cust_email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    cust_bill_card = CardNumberField('card number')
    cust_bill_expiry = CardExpiryField('expiration date')
    cust_bill_code = SecurityCodeField('security code')
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_email)


class Employee(models.Model):
    role = models.CharField(max_length=50, choices=Roles, default='employee')
    emp_first_name = models.CharField(max_length=50)
    emp_last_name = models.CharField(max_length=50)
    emp_email = models.EmailField(max_length=100, null=False, blank=False)
    emp_id = models.IntegerField(blank=False, null=False)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.emp_email)
