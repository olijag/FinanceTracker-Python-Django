from django.shortcuts import redirect
from ..NewTransactionForm import NewTransactionForm


def addNewTransaction(request, account):
    form = NewTransactionForm(request.POST)
    if form.is_valid():
        # No need to fetch main_account again if it's already fetched
        new_transaction = form.save(commit=False)
        new_transaction.account = account
        new_transaction.save()
        return redirect('testing')  # Redirect to a success page, not the template itself
    else:
        form = NewTransactionForm()  # Initialize an unbound form for GET requests