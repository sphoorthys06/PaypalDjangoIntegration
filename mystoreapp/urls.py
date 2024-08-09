from django.urls import path
from .views import ItemView

urlpatterns = [
    path('', ItemView, name='items'),
]