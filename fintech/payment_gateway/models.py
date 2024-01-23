from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.amount} - {self.description}"

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    stripe_payment_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"${self.amount} - {self.description}"


