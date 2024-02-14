from django.urls import path
from . import views

urlpatterns = [
	path('api/v1/init', views.init, name='init'),
	path('api/v1/wallet', views.wallet, name='wallet'),
]
