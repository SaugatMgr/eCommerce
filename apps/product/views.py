from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from apps.product.forms import ProductForm

from .models import Product


class HomePageView(TemplateView):
    model = Product
    template_name = "main/home/home.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class AddProductView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = "main/home/product/add_product.html"
    success_url = reverse_lazy("home")


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = "main/home/product/product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs["slug"])


class UpdateProductView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = "main/home/product/update_product.html"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    template_name = "main/home/product/delete_product.html"
    success_url = reverse_lazy("home")
    context_object_name = "product"


class LikeProductView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        product_slug = request.POST.get("product_slug")
        product = Product.objects.get(slug=product_slug)
        user = request.user

        if product.liked_by.filter(id=user.id).exists():
            product.liked_by.remove(user)
            product.likes -= 1
        else:
            product.liked_by.add(user)
            product.likes += 1
        product.save()

        return HttpResponseRedirect(reverse_lazy("home"))


class SearchResultsView(TemplateView):
    template_name = "search_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        if query:
            results = Product.objects.filter(name__icontains=query)
            context["results"] = results
            context["query"] = query
        return context


# class LikeProductView(View):
#     def post(self, request, *args, **kwargs):
#         import pdb

#         pdb.set_trace()
#         ajax_format = request.headers.get("x-requested-with")
#         product_slug = request.POST.get("product_slug")
#         product = Product.objects.get(slug=product_slug)
#         user = request.user

#         if ajax_format == "XMLHttpRequest":
#             if product.liked_by.filter(id=user.id).exists():
#                 product.liked_by.remove(user)
#                 return JsonResponse(
#                     {
#                         "success": True,
#                         "message": f"You disliked {product.name}.",
#                     },
#                     status=201,
#                 )
#             else:
#                 product.liked_by.add(user)
#                 return JsonResponse(
#                     {
#                         "success": True,
#                         "message": f"You liked {product.name}.",
#                     },
#                     status=201,
#                 )
#         else:
#             return JsonResponse(
#                 {
#                     "success": False,
#                     "message": "Cannot process.Must be and AJAX XMLHttpRequest.",
#                 },
#                 status=400,
#             )
