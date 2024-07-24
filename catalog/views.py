from django.shortcuts import render
from catalog.models import *
from django.core.paginator import Paginator


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name, email)
    elif request.method == 'GET':
        product_list = Product.objects.all()
        context = {'objects': product_list}
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, message)

    if request.method == 'GET':
        context = {'object': User.objects.last()}
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    if request.method == 'GET':
        current_product = Product.objects.get(pk=pk)
        current_category = Category.objects.get(id=current_product.category_id)
        context = {'object': current_product,
                   'category': current_category.name
                   }
    return render(request, 'catalog/product.html', context)


def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        paginator = Paginator(products, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'catalog/products.html', {'page_obj': page_obj})