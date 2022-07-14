from . import views
from django.urls import path

urlpatterns=[
    path('cartDetails', views.cart_details, name='cartDetails'),
    path('add<int:product_id>/', views.add_cart, name='addcart'),
    path('decrement_cart/<int:product_id>/',views.min_cart,name='dec_cart'),
    path('remove/<int:product_id>/',views.min_cart,name='remove'),
]