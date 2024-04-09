from django.urls import path

from .views import HomePageView, AddProductView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("product/add-product/", AddProductView.as_view(), name="add-product"),
]
