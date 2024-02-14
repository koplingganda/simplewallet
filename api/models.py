from django.db import models


class Account(models.Model):
	customer_xid = models.CharField(max_length=255, primary_key=True)
	token = models.CharField(max_length=255)
	created_datetime = models.DateTimeField()


class Wallet(models.Model):
	owned_by = models.OneToOneField(
		Account,
		on_delete=models.CASCADE
	)
	status = models.CharField(max_length=255)
	enabled_at = models.DateTimeField(null=True)
	disabled_at = models.DateTimeField(null=True)
	balance = models.DecimalField(max_digits=12, decimal_places=2)


class Ledger(models.Model):
	customer_xid = models.CharField(max_length=255)
	transaction_datetime = models.DateTimeField()
	status = models.CharField(max_length=255)
	reference_id = models.CharField(max_length=255, unique=True)
	amount = models.DecimalField(max_digits=12, decimal_places=2)
