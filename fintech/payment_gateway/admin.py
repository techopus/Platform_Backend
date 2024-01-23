from django.contrib import admin

# Register models here.

from .models import Transaction, Payment

admin.site.register(Transaction)
admin.site.register(Payment)
