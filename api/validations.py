from api.models import Wallet, Ledger


def validate_wallet_status(account_obj):
	is_wallet_enabled = Wallet.objects.filter(owned_by=account_obj.customer_xid, status="enabled").first()

	if not is_wallet_enabled:
		raise Exception("Wallet is disabled")


def validate_reference_id(reference_id):
	is_reference_id_exist = Ledger.objects.filter(reference_id=reference_id).first()

	if is_reference_id_exist:
		raise Exception("Duplicate reference ID")


def validate_wallet_balance(balance_amount, withdraw_amount):
	if balance_amount < withdraw_amount:
		raise Exception("Insufficient balance")
