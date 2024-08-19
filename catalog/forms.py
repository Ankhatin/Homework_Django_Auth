from django import forms
from django.forms import BooleanField
from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                pass #field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class DisableWidgetMixin:
    def __init__(self, *args, **kwargs):
        is_disabled = kwargs.pop('is_disabled')
        is_super = kwargs.pop('is_super')
        disabled_fields = ('description', 'category', 'is_published')
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if is_disabled and not is_super:
                if field_name not in disabled_fields:
                    field.widget.attrs['disabled'] = True


class ProductForm(DisableWidgetMixin, StyleMixin, forms.ModelForm):
    vorbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('user',)


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     is_disabled = kwargs.pop('disabled')
    #     if is_disabled:

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        for word in ProductForm.vorbidden_words:
            if word in cleaned_name:
                raise forms.ValidationError(f'Слово {word} нельзя употреблять в названии продукта')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        for word in ProductForm.vorbidden_words:
            if word in cleaned_description:
                raise forms.ValidationError(f'Слово {word} нельзя употреблять в описании продукта')
        return cleaned_description


class VersionForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
