from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Product
from .forms import ProductModelForm
from django.urls import reverse_lazy

import locale
locale.setlocale(locale.LC_MONETARY, 'pt_br.UTF-8')


class ProductsListView(ListView):
    template_name = 'products.html'
    model = Product

    def value_total(self, product):
        product.value_total = locale.currency(product.price * product.quantity)
        product.price_format = locale.currency(product.price)
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context["products"] = map(self.value_total, list(Product.objects.order_by('name').all()))
        context["name_page"] = 'Home'
        return context
    

class DetailProductView(DetailView):
    model = Product
    template_name = 'detailproduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.get(id=self.kwargs['pk'])
        return context
        
       
class CreateProductView(CreateView):
    model = Product
    fields = ['name', 'quantity', 'price']
    template_name = 'createproduct.html'
    success_url = reverse_lazy('products')


class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
    template_name = 'deleteproduct.html'


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'updateproduct.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')


  
            

    

    
 


    
