from django.contrib import admin
from .models import Account, Transaction

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "balance")

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "amount", "date", "account")



admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)