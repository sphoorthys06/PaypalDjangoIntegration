from django.urls import path
from .views import BuyItem, Successfulpayment, Failedpayment

urlpatterns = [
    path('BuyItem/<int:item_id>/', BuyItem, name='BuyItem'),
    path('Successfulpayment/<int:item_id>/', Successfulpayment, name='Successfulpayment'),
    path('Failedpayment/<int:item_id>/', Failedpayment, name='Failedpayment'),
]