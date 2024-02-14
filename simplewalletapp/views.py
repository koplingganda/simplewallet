from django.shortcuts import render
from django.http import HttpResponse


def simplewalletapp(request):
	return HttpResponse("Hello world!")
