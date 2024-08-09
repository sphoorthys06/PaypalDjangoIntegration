from django.shortcuts import render
from .models import Items

def ItemView(request):

    get_items = Items.objects.all()

    return render(request, 'items.html', {'items': get_items})
