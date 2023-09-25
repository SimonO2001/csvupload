# shop/views.py

from django.shortcuts import render
from django.views.generic.base import View
from csv import DictReader
from io import TextIOWrapper
from django.shortcuts import render, redirect  # Import redirect

from .forms import UploadForm, ProductForm


class UploadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "upload.html", {"form": UploadForm()})
    
    def post(self, request, *args, **kwargs):
        products_file = request.FILES["products_file"]
        rows = TextIOWrapper(products_file)
        for row in DictReader(rows):
            form = ProductForm(row)
            form.save()
        return render(request, "upload.html", {"form": UploadForm()})
