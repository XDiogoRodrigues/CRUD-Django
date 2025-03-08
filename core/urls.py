from django.urls import path
from .views import ProductsListView, DetailProductView, CreateProductView, DeleteProductView, UpdateProductView

urlpatterns = [ 
    path('', ProductsListView.as_view(), name='products'),
    path('detail/<int:pk>/', DetailProductView.as_view(), name='detail'),
    path('createproduct/', CreateProductView.as_view(), name='create'),
    path('deleteproduct/<int:pk>/', DeleteProductView.as_view(), name='delete'),
    path('updateproduct/<int:pk>/', UpdateProductView.as_view(), name='update'),
]