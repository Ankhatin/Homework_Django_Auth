from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django import forms
from catalog.forms import ProductForm, VersionForm
from catalog.models import *
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView

from catalog.services import get_cached_categories


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_list = Product.objects.all()
        context_data['product_versions'] = {}
        for product in product_list:
            if len(product.versions.filter(is_current=True)):
                version = product.versions.filter(is_current=True).last()
                context_data['product_versions'].update({product: version})
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    login_url = '/users/login/'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = self.request.user
        product = form.save()
        product.user = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    login_url = '/users/login/'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_kwargs(self, **kwargs):
        kwargs = super(ProductUpdateView, self).get_form_kwargs()
        kwargs.update({'is_disabled': self.request.user.has_perm('catalog.set_published'),
                       'is_super': self.request.user.is_superuser})
        return kwargs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        counter = 0
        for form_version in formset:
            if form_version.is_valid():
                if form_version.cleaned_data.get('is_current'):
                    counter += 1
        if counter > 1:
            form.add_error(None, ValidationError('Только одна версия товара может быть активной'))
            return self.form_invalid(form)
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        context_data = self.get_context_data()
        context_data['form'] = form
        return self.render_to_response(context_data)


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    login_url = '/users/login/'
    success_url = reverse_lazy('catalog:product_list')


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects'] = get_cached_categories()
        return context_data


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}
