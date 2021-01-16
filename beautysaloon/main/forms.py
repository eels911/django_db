from .models import Visits
from django.forms import ModelForm, TextInput, NumberInput
from django import forms


class PriceFilterForm(forms.Form):
    price_min = forms.IntegerField(label="От", required=False)
    price_max = forms.IntegerField(label="До", required=False)


class VisitsForm(ModelForm):
    class Meta:
        model = Visits
        fields = ["visit_number", "service_name", "fio_client", "fio_staff","price"]
        widgets = {
            "visit_number": NumberInput(attrs={
                'id': 'visit_number',
                'class': 'form-control',
                'placeholder': 'Введите номер клиента...'
            }),
            "service_name": TextInput(attrs={
                'id': 'service_name',
                'class': 'form-control',
                'placeholder': 'Введите тип услуги...'
            }),
            "fio_client": TextInput(attrs={
                'id': 'fio_client',
                'class': 'form-control',
                'placeholder': 'Выберите фио клиента...'
            }),
            "fio_staff": TextInput(attrs={
                'id': 'fio_staff',
                'class': 'form-control',
                'placeholder': 'Введите фио работника...'
            }),
            "price": NumberInput(attrs={
                'id': 'price',
                'class': 'form-control',
                'placeholder': 'Введите цену...'
            }),
        }