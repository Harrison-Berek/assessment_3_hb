from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/create/', views.ItemsCreate.as_view(), name='items_create'),
    path('items/<int:item_id>/', views.items_delete, name='items_delete'),
]