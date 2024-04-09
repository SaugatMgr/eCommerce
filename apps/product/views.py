from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.product.forms import ProductForm

from .models import Product

class HomePageView(TemplateView):
    model = Product
    template_name = 'main/home/home.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/home/product/add_product.html'
    success_url = reverse_lazy('home')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/home/product/product_detail.html'
    
    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs["slug"])

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/home/product/update_product.html'
    
    def get_success_url(self):
        return self.object.get_absolute_url()

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/home/product/delete_product.html'
    success_url = reverse_lazy('home')
    context_object_name = 'product'