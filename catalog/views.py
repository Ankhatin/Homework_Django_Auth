from django.shortcuts import render
from catalog.models import *
from django.core.paginator import Paginator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView


class ProductListView(ListView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product

