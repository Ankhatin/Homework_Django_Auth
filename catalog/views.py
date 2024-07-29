from django.shortcuts import render
from catalog.models import *
from django.core.paginator import Paginator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


class ProductListView(ListView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты' }


class ProductDetailView(DetailView):
    model = Product

