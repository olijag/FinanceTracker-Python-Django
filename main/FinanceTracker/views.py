from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def main(request):
    template = loader.get_template('index.html')
    
    def format_usa_balance(number):
        return f"{number:,.2f}"

    spendings = 5326.00
    income = 14074.00
    balance = income - spendings

    context = {
        'spendings': format_usa_balance(spendings),
        'income': format_usa_balance(income),
        'balance': format_usa_balance(balance),
    }
    return HttpResponse(template.render(context, request))