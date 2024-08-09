from django.shortcuts import render
from mystoreapp.models import Items
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse


def BuyItem(request, item_id):

    item = Items.objects.get(id=item_id)
    hardcoded_user_id = 1
    host = request.get_host()
    invoice_id = f"{uuid.uuid4()}-{hardcoded_user_id}"
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': item.price,
        'item_name': item.name,
        'invoice': invoice_id,
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('Successfulpayment', kwargs = {'item_id': item.id})}",
        'cancel_url': f"http://{host}{reverse('Failedpayment', kwargs = {'item_id': item.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'item': item,
        'paypal': paypal_payment
    }

    return render(request, 'BuyItem.html', context)

def Successfulpayment(request, item_id):

    item = Items.objects.get(id=item_id)

    return render(request, 'successfullpayment.html', {'item': item})

def Failedpayment(request, item_id):

    item = Items.objects.get(id=item_id)

    return render(request, 'failedpayment.html', {'item': item})
