# shop/forms.py

from django.forms import FileField, Form, ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["Location", "Customer_id", "MAC", "Model", "S_N", "Name", "Image", "GW_IP", "Notes", "Journalsystem", "Analyzers", "SIM"]


class UploadForm(Form):
    products_file = FileField()