from django.http import HttpResponse
from django.shortcuts import redirect
from ..models import Transaction
from ..NewTransactionForm import NewTransactionForm

def delete_transaction(request, transaction_id):
    if request.method == 'POST':
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.delete()
        return redirect('testing')
    else:
        return HttpResponse("Method not allowed", status=405)