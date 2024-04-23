from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Account, Transaction
from .NewTransactionForm import NewTransactionForm

# Global functions 
def format_usa_balance(number):
        number = float(number)
        return f"{number:,.2f}"


# Main
def main(request):
    template = loader.get_template('index.html')

    main_account = Account.objects.get(name="main")
    transactions_main_account = main_account.transactions.all()    
    balance = main_account.balance

    spendings = 5326.00
    income = 14074.00
    

    context = {
        'main_account': main_account,
        'transactions_main_account': transactions_main_account,
        'balance': format_usa_balance(balance), 
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    template = loader.get_template('testing.html')

    accounts = Account.objects.all().values()
    main_account = Account.objects.get(name="main")
    transactions_main_account = main_account.transactions.all()

    form = NewTransactionForm() 
    
    context = {
         'accounts': accounts,
         'main_account': main_account,
         'transactions_main_account': transactions_main_account,
         'form': form,
    }  

    return HttpResponse(template.render(context, request))