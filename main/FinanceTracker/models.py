from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
    notes = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        return f"{self.title} on {self.date} - Amount: {self.amount}"


