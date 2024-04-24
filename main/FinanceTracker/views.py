from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Account, Transaction
from .NewTransactionForm import NewTransactionForm


def format_usa_balance(number):
    number = float(number)
    return f"{number:,.2f}"

# ==== Main
def main(request):
    template = loader.get_template('index.html')

    # Define variables 
    main_account = Account.objects.get(name="main")
    transactions_main_account = main_account.transactions.all().order_by('-date')   
    balance = main_account.balance

    # Define the http post request from the Add New Transaction form
    if request.method == 'POST':
        form = NewTransactionForm(request.POST)
        if form.is_valid():
            # No need to fetch main_account again if it's already fetched
            new_transaction = form.save(commit=False)
            new_transaction.account = main_account
            new_transaction.save()
            return redirect('main')  # Redirect to a success page, not the template itself
    else:
        form = NewTransactionForm()  # Initialize an unbound form for GET requests
    

    context = {
         'main_account': main_account,
         'transactions_main_account': transactions_main_account,
         'form': form,
    }

    return render(request, "index.html", context)


     


def testing(request):
    template = loader.get_template('testing.html')

    # Fetch accounts and main account
    main_account = Account.objects.get(name="main")
    transactions_main_account = main_account.transactions.all().order_by('-date')

    if request.method == 'POST':
        form = NewTransactionForm(request.POST)
        if form.is_valid():
            # No need to fetch main_account again if it's already fetched
            new_transaction = form.save(commit=False)
            new_transaction.account = main_account
            new_transaction.save()
            return redirect('testing')  # Redirect to a success page, not the template itself
    else:
        form = NewTransactionForm()  # Initialize an unbound form for GET requests

    context = {
         'main_account': main_account,
         'transactions_main_account': transactions_main_account,
         'form': form,
    }  

    return render(request, "testing.html", context)