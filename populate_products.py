import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_shop.settings')
django.setup()

from shop.models import Product

# stripe_product_id, stripe_price_id, name, description, price

products = [
    {'stripe_product_id': 'prod_Qik40V4lxABH9G', 'stripe_price_id': 'price_1PrIaMEN9TFKicCwDW2XyjrW', 'name': 'T-shirt', 'description': 'Comfortable cotton t-shirt', 'price': 19.99},
    {'stripe_product_id': 'prod_Qik6Og3avQoxBk', 'stripe_price_id': 'price_1PrIciEN9TFKicCw3UPuYv2q', 'name': 'Jeans', 'description': 'Stylish denim jeans', 'price': 49.99},
    {'stripe_product_id': 'prod_Qik8EnbGI1ncqJ', 'stripe_price_id': 'price_1PrIeLEN9TFKicCwmkyhQPIm', 'name': 'Sneakers', 'description': 'Sporty sneakers', 'price': 89.99},
    {'stripe_product_id': 'prod_Qik9NNNf6x5XW8', 'stripe_price_id': 'price_1PrIerEN9TFKicCwj60Zne0x', 'name': 'Jacket', 'description': 'Warm winter jacket', 'price': 129.99},
    {'stripe_product_id': 'prod_Qik9Tva0e3bfbk', 'stripe_price_id': 'price_1PrIfMEN9TFKicCwvJ3iL9yS', 'name': 'Hat', 'description': 'Baseball Cap', 'price': 14.99},
    {'stripe_product_id': 'prod_QikAniGnpJOmjy', 'stripe_price_id': 'price_1PrIgkEN9TFKicCwpMcLTIEL', 'name': 'Socks', 'description': 'Comfortable socks', 'price': 11.99},
    {'stripe_product_id': 'prod_QikCOknjDjkCdT', 'stripe_price_id': 'price_1PrIhpEN9TFKicCwRAfU8eVr', 'name': 'Shorts', 'description': 'Cargo shorts', 'price': 24.99},
    {'stripe_product_id': 'prod_QikCTZssAO3ykI', 'stripe_price_id': 'price_1PrIiQEN9TFKicCwTCR7lOCs', 'name': 'Hooded Sweatshirt', 'description': 'Insulated Sweatshirt', 'price': 34.99},
]

for product in products:
    Product.objects.create(**product)

print("Products added successfully!")