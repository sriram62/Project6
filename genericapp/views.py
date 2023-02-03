from django.shortcuts import render
from.models import product
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.list import ListView

class ProductUpdateView(UpdateView):
    model = product
    fields = ["pname","pcost"]
    success_url ="/"
class ProductsListView(ListView):
    model = product
class ProductDeleteView(DeleteView):
    model = product
    success_url = "/"
