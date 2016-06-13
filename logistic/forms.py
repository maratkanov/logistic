from django import forms

from logistic import models


class SimpleRequestForm(forms.ModelForm):
    class Meta:
        model = models.SimpleRequestModel
        fields = ['name', 'email', 'phone']


class RequestForm(forms.ModelForm):
    class Meta:
        model = models.RequestModel
        fields = [
            'name', 'company', 'email', 'phone', 'ship_date', 'from_address', 'to_address',
            'price', 'amount', 'weight', 'code', 'size', 'places'
        ]
