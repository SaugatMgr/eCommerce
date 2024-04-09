from django.urls import path

from .views import HomePageView, AddProductView, ProductDetailView, UpdateProductView, ProductDeleteView, LikeProductView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("product/add-product/", AddProductView.as_view(), name="add-product"),
    path('product/like-product/', LikeProductView.as_view(), name='like-product'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<slug:slug>/update/', UpdateProductView.as_view(), name='update-product'),
    path('product/<slug:slug>/delete/', ProductDeleteView.as_view(), name='delete-product'),
]
