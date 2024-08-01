from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price', 'description', 'image']
        widgets = {
            'name' : forms.TextInput(attrs={'required' : '', 'Placeholder' : 'Product name'}),
            'quantity' : forms.NumberInput(attrs={'required' : '', 'Placeholder' : 'Product quantity'}),
            'price' : forms.NumberInput(attrs={'required' : '', 'Placeholder' : 'Product price'}),
            'description' : forms.Textarea(attrs={'required' : '', 'Placeholder' : 'Product description'}),
        }