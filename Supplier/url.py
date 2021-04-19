from django.urls import path
from .views import SupplierCreateView, SupplierListView, SupplierDetailView, SupplierUpdateView, Supplier_confirm_delete

urlpatterns = [
    path('SupplierCreateView/', SupplierCreateView.as_view(), name='SupplierCreateView'),
    path('SupplierListView/', SupplierListView.as_view(), name='SupplierListView'),
    path('SupplierDetailView/<int:pk>/', SupplierDetailView.as_view(), name='SupplierDetailView'),
    path('SupplierUpdateView/<int:pk>/<str:SupplierName>/', SupplierUpdateView.as_view(), name='SupplierUpdateView'),
    path('Supplier_confirm_delete/<int:pk>/', Supplier_confirm_delete.as_view(), name='Supplier_confirm_delete')
]
