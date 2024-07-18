from django.shortcuts import render
from catalog.models import *


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)
    elif request.method == 'GET':
        product_list = Product.objects.order_by('-pk')[:5:-1]
        for product in product_list:
            print(product)
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, message)
    if request.method == 'GET':
        last_user = User.objects.last()
        name = last_user.name
        phone = last_user.phone
        request.GET = request.GET.copy()
        request.GET.update({'name': name, 'phone': phone})
    return render(request, 'catalog/contacts.html')
