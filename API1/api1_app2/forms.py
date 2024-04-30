from django import forms
from api1_app2.models import Product

class ProductForm(forms.ModelForm):
     class Meta:
          model = Product
          fields = ['title','content','price']