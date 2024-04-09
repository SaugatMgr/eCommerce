from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
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

    def form_valid(self, form):
        import pdb;pdb.set_trace()
        return super().form_valid(form)