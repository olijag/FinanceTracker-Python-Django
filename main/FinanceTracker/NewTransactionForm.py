from django import forms
from .models import Transaction

class NewTransactionForm(forms.ModelForm):
     class Meta:
        model = Transaction
        fields = ['title', 'amount', 'date', 'notes']
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'titleHelp'}),
          'amount': forms.NumberInput(attrs={'class': 'form-control', 'aria-describedby': 'amountHelp'}),
          'date': forms.DateTimeInput(attrs={'class': 'form-control', 'aria-describedby': 'dateHelp', 'type': 'datetime-local'}),
          'notes': forms.Textarea(attrs={'class': 'form-control', 'aria-describedby': 'notesHelp'}),
        }