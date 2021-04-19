from django.urls import path
from .views import AssetCreateView, AssetDetailView
from .import views
from django.views.generic import TemplateView


urlpatterns = [
    path('Equipment/', AssetCreateView.as_view(), name='asset'),
    path('search/', views.search, name='search'),
    path('AssetDetailView/<int:pk>/', AssetDetailView.as_view(), name='AssetDetailView'),
    path('EquipmentEconomic_Form/', TemplateView.as_view(template_name='Asset/EquipmentEconomic_Form.html'), name='EquipmentEconomic_Form'),
    path('EquipmentTechnical_Form/', TemplateView.as_view(template_name='Asset/EquipmentTechnical_Form.html'),
         name='EquipmentTechnical_Form'),
    path('EquipmentMaintenance_Form/', TemplateView.as_view(template_name='Asset/EquipmentMaintenance_Form.html'),
         name='EquipmentMaintenance_Form'),

]
