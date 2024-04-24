from django.shortcuts import render, redirect
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

    # Fetch accounts and main account
    accounts = Account.objects.all().values()
    main_account = Account.objects.get(name="main")

    # Initialize form outside the POST check to handle both GET and POST
    form = NewTransactionForm() 
    if request.method == 'POST':
        form = NewTransactionForm(request.POST)
        # Extract data from form directly
        title = form.Meta['title']
        amount = form.Meta['amount']
        date = form.Meta['date']
        notes = form.Meta['notes']

        # Create and save new transaction
        new_transaction = Transaction(title=title, amount=amount, date=date, notes=notes, account=main_account)
        new_transaction.save()
        return redirect('testing')
    else:
        form = NewTransactionForm()

    transactions_main_account = main_account.transactions.all()


    context = {
         'accounts': accounts,
         'main_account': main_account,
         'transactions_main_account': transactions_main_account,
         'form': form,
    }  

    return HttpResponse(template.render(context, request))