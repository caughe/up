from django.contrib import admin

from .models import Customer


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_email', 'cust_id', 'phone_number')
    list_filter = ('cust_email', 'cust_id')
    search_fields = ('cust_id',)
    ordering = ['cust_id']


admin.site.register(Customer)
