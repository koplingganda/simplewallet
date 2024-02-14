import json
import random
import string

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Account, Wallet, Ledger


@csrf_exempt
@api_view(["POST"])
def init(request):
	try:
		data = request.POST.dict()
		token = ''.join(random.choices(string.ascii_letters + string.digits, k=42))

		account = Account(
			customer_xid=data.get("customer_xid"),
			token=token,
			created_datetime=datetime.now()
		)
		account.save()

		res = {
			"data": {
				"token": token
			},
			"status": "success"
		}
	except Exception as e:
		res = {
			"data": {
				"error": repr(e)
			},
			"status": "fail"
		}

	return HttpResponse(json.dumps(res), content_type='application/json')


@csrf_exempt
@api_view(["POST", "PATCH", "GET"])
def wallet(request):
	res = {}

	try:
		token = request.headers.get("Authorization").split("Token ")
		account_obj = Account.objects.get(token=token[1])

		if request.method in ("POST", "PATCH"):
			res = change_wallet_status(account_obj, request)
		elif request.method == "GET":
			res = get_wallet(account_obj)

	except Exception as e:
		res = {
			"data": {
				"error": repr(e)
			},
			"status": "fail"
		}

	return HttpResponse(json.dumps(res), content_type='application/json')


def change_wallet_status(account_obj, request):
	data = request.data
	is_wallet_exist = Wallet.objects.filter(owned_by=account_obj.customer_xid).first()

	if not is_wallet_exist and not data.get("is_disabled"):
		wallet_obj = Wallet(
			owned_by=account_obj,
			status="enabled",
			enabled_at=datetime.now(),
			balance=0
		)
		wallet_obj.save()

		return {
			"data": {
				"id": wallet_obj.id,
				"owned_by": account_obj.customer_xid,
				"status": wallet_obj.status,
				"enabled_at": str(wallet_obj.enabled_at),
				"balance": float(wallet_obj.balance)
			},
			"status": "success"
		}

	elif is_wallet_exist and not data.get("is_disabled"):
		wallet_obj = Wallet.objects.get(owned_by=account_obj.customer_xid)

		wallet_obj.status = "enabled"
		wallet_obj.enabled_at = datetime.now()
		wallet_obj.save()

		return {
			"data": {
				"id": wallet_obj.id,
				"owned_by": account_obj.customer_xid,
				"status": wallet_obj.status,
				"enabled_at": str(wallet_obj.enabled_at),
				"balance": float(wallet_obj.balance)
			},
			"status": "success"
		}

	elif is_wallet_exist and data.get("is_disabled"):
		wallet_obj = Wallet.objects.get(owned_by=account_obj.customer_xid)

		wallet_obj.status = "disabled"
		wallet_obj.disabled_at = datetime.now()
		wallet_obj.save()

		return {
			"data": {
				"id": wallet_obj.id,
				"owned_by": account_obj.customer_xid,
				"status": wallet_obj.status,
				"disabled_at": str(wallet_obj.disabled_at),
				"balance": float(wallet_obj.balance)
			},
			"status": "success"
		}

	else:
		return {
			"data": {
				"error": "Invalid operation"
			},
			"status": "fail"
		}


def get_wallet(account_obj):
	wallet_obj = Wallet.objects.get(owned_by=account_obj.customer_xid)

	return {
		"data": {
			"id": wallet_obj.id,
			"owned_by": account_obj.customer_xid,
			"status": wallet_obj.status,
			"enabled_at": str(wallet_obj.enabled_at),
			"disabled_at": str(wallet_obj.disabled_at),
			"balance": float(wallet_obj.balance)
		},
		"status": "success"
	}


@csrf_exempt
def deposits(request):
	print(request)


@csrf_exempt
def withdrawals(request):
	print(request)
