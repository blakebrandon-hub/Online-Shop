from django.template import TemplateDoesNotExist
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from simple_shop import settings
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import stripe
import json

stripe.api_key = 'sk_test_51KLvUgEN9TFKicCwkQeO58hk4k8MTpckjs1Uzp7I6Yy093aq8e50pvmqHqap5CQsPvEMgunbdv13iHMTLUwyjJ7b00shqxRsuz'

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def detail(request, product_id):
    product = stripe.Product.retrieve(product_id)
    price = stripe.Price.list(product=product_id, limit=1)
    price_int = int(price.data[0].unit_amount)
    price_formatted = price_int / 100

    return render(request, 'shop/detail.html', {
        'product': product,
        'price': price_formatted,
        'stripe_public_key': 'pk_test_51KLvUgEN9TFKicCwT1Owl6YPE9FIzhh4nhJECAR0eqVicJHpLfFlJnK5ZiMbwP6rhIhHjAgBILCY5iw7Rp5NTNdS00YnKgJI75'
    })

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1,
                    } for price_id in data['price_ids']
                ],
                mode='payment',
                success_url='http://127.0.0.1:8000/success/',
                cancel_url='http://127.0.0.1:8000/cancel/',
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# Success and Cancel views
def payment_success(request):
    return render(request, 'shop/success.html')

def payment_cancel(request):
    return render(request, 'shop/cancel.html')