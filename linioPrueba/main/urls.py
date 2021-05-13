from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Inicio', views.Saludo, name='saludo'),
    path('productos', views.ProductListView.as_view(), name='product-list'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('Localizacion', views.LocalListView.as_view(), name='Local-list'),
    path('Localizacion/<int:pk>', views.LocalDetailView.as_view(), name='Local-detail'),

]
