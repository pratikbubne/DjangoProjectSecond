from django.urls import path
from .views import AssetModelCreateView, AssetModelListView, AssetModelUpdateView, AssetModel_confirm_delete

urlpatterns = [
    path('AssetModelCreateView/', AssetModelCreateView.as_view(), name='AssetModelCreateView'),
    path('AssetModelListView/', AssetModelListView.as_view(), name='AssetModelListView'),
    path('AssetModelUpdateView/<int:pk>/', AssetModelUpdateView.as_view(), name='AssetModelUpdateView'),
    path('AssetModel_confirm_delete/<int:pk>/', AssetModel_confirm_delete.as_view(), name='AssetModel_confirm_delete')
]
