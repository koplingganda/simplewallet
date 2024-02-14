from django.urls import path
from . import views

urlpatterns = [
	path('api/v1/init', views.init, name='init'),
	path('api/v1/wallet', views.wallet, name='wallet'),
	path('api/v1/wallet/transactions', views.transactions, name='transactions'),
	path('api/v1/wallet/deposits', views.deposits, name='deposits'),
	path('api/v1/wallet/withdrawals', views.withdrawals, name='withdrawal')
]
