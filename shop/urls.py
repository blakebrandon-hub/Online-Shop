from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<str:product_id>/', views.detail, name='product_detail'),  
    path('create_checkout_session/', views.create_checkout_session, name='checkout'),
    path('success/', views.payment_success, name='success'),
    path('cancel/', views.payment_cancel, name='cancel')
]