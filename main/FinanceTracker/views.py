from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Sum

# Models 
from .models import Account, Transaction

# Functions and classes
from .NewTransactionForm import NewTransactionForm
from .requestsPOST.addNewTransaction import addNewTransaction
from .requestsPOST.deleteTransaction import delete_transaction


def format_usa_balance(number): # This minimal functions makes it easy to convert the argument to a format of USA currency eg. 19,300.99
    number = float(number)
    return f"{number:,.2f}"

# ==== Main
def main(request):
    template = loader.get_template('index.html')

    # Define variables 
    main_account = Account.objects.get(name="main")
    transactions_main_account = main_account.transactions.all().order_by('-date')   
    
    # Calculate total balance 
    balance = transactions_main_account.aggregate(Sum('amount'))['amount__sum'] or 0 
    balance = format_usa_balance(balance)

    form = NewTransactionForm()

    # Define the http post request from the Add New Transaction form
    if request.method == 'POST': # Handle incoming post requests
        if 'action' in request.POST: # Check which post request it is, this is checking the parameter "name" and "value" in the button-tag in html file
            if request.POST['action'] == 'add_new_transaction':
                # Handling the action for adding a new transaction
                addNewTransaction(request, main_account)
                return redirect('main')  # Ensure to redirect after handling POST to avoid re-posting on refresh
            elif request.POST['action'] == 'delete_transaction':
                transaction_id = request.POST.get('transaction_id')  # Get transaction_id from POST data
                if transaction_id:
                    delete_transaction(request, transaction_id)
                    return redirect('main')  # Redirect to the same page to reflect the deletion
                else:
                    return HttpResponse("Transaction ID not specified", status=400)
            else:
                return HttpResponse("No action specified", status=400)
        else:
            # This will handle any other POST that doesn't specify an action
            return HttpResponse("Action not found", status=400)
    else:
        # Handle GET request normally by displaying the page
        context = {
            'main_account': main_account,
            'transactions_main_account': transactions_main_account,
            'form': form,
            'balance': balance,
        }  
        return render(request, "index.html", context)


     

#=== Testing
def testing(request):
    template = loader.get_template('testing.html')

    # Fetch accounts and main account
    main_account = Account.objects.get(name="main")
    transactions_main_account = main_account.transactions.all().order_by('-date')
    form = NewTransactionForm()

    balance = transactions_main_account.aggregate(Sum('amount'))['amount__sum'] or 0  # Calculate total balance
    balance = format_usa_balance(balance)

    if request.method == 'POST': # Handle incoming post requests
        if 'action' in request.POST: # Check which post request it is, this is checking the parameter "name" and "value" in the button-tag in html file
            if request.POST['action'] == 'add_new_transaction':
                # Handling the action for adding a new transaction
                addNewTransaction(request, main_account)
                return redirect('testing')  # Ensure to redirect after handling POST to avoid re-posting on refresh
            elif request.POST['action'] == 'delete_transaction':
                transaction_id = request.POST.get('transaction_id')  # Get transaction_id from POST data
                if transaction_id:
                    delete_transaction(request, transaction_id)
                    return redirect('testing')  # Redirect to the same page to reflect the deletion
                else:
                    return HttpResponse("Transaction ID not specified", status=400)
            else:
                return HttpResponse("No action specified", status=400)
        else:
            # This will handle any other POST that doesn't specify an action
            return HttpResponse("Action not found", status=400)
    else:
        # Handle GET request normally by displaying the page
        context = {
            'main_account': main_account,
            'transactions_main_account': transactions_main_account,
            'form': form,
            'balance': balance,
        }  
        return render(request, "testing.html", context)


