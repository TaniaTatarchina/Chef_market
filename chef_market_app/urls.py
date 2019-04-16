from django.urls import path
from chef_market_app import views


urlpatterns = [
    path('dishes/<dish_id>/', views.dish_detail_view, name='dish_detail'),
    path('dishes/', views.dishes_list_view, name='dishes_list'),
    path('basket/', views.basket_view, name='basket'),
    path('basket/pay/', views.pay_view, name='pay'),

]

