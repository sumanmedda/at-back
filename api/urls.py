from django.urls import path
from .views import ProductsViews

urlpatterns = [
    path('all-products/', ProductsViews.as_view(), name="all-products"),
    path('add-product/', ProductsViews.as_view(), name="add-product"),

]
