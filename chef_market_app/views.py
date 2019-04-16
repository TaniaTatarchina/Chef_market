from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from chef_market_app.models import Dish, Order


def dishes_list_view(request):
    dishes_list = Dish.objects.all().order_by('name')
    context = {'dishes_list': dishes_list}
    return render(request, 'chef_market_app/dishes_list.html', context=context)


@login_required(login_url='/login/')
def dish_detail_view(request, dish_id):
    dish = Dish.objects.get(id=dish_id)

    if request.method == 'GET':
        context = {'dish': dish}
        return render(request, 'chef_market_app/dish_detail.html', context=context)

    elif request.method == 'POST':
        Order.objects.create(customer=request.user, dish=dish)
        return redirect('basket')


@login_required(login_url='/login/')
def basket_view(request):
    orders = Order.objects.filter(customer=request.user).order_by('-create_date')

    if request.method == 'POST':
        orders.get(id=request.POST['order_id']).delete()

    total_price = 0

    for order in orders:
        total_price += order.dish.price

    context = {
        'orders': orders,
        'total_price': total_price
    }
    return render(request, 'chef_market_app/basket.html', context=context)


@login_required(login_url='/login/')
def pay_view(request):
    if request.method == 'POST':
        Order.objects.filter(customer=request.user).delete()
        return redirect('dishes_list')
