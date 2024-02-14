from django.urls import path
from . import views

urlpatterns = [
	path('simplewalletapp/', views.simplewalletapp, name='simplewalletapp'),
]
