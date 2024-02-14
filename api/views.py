import json

from django.shortcuts import render
from django.http import HttpResponse


def init(request):
	var = {
		"data": "HELLO",
		"status": "Palsu"
	}

	return HttpResponse(json.dumps(var), content_type='application/json')


def wallet(request):
	var = {
		"data": "HELLO",
		"status": "Palsu",
		"request": "1"
	}

	return HttpResponse(json.dumps(var), content_type='application/json')
