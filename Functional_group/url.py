from django.urls import path
from .views import FunctionalGroupListView, FunctionalGroupCreateView, FunctionalGroupUpdateView, FunctionalGroup_confirm_delete

urlpatterns = [
    path('FunctionalGroupListView/', FunctionalGroupListView.as_view(), name='FunctionalGroupListView'),
    path('FunctionalGroupCreateView/', FunctionalGroupCreateView.as_view(), name='FunctionalGroupCreateView'),
    path('FunctionalGroupUpdateView/<int:pk>/', FunctionalGroupUpdateView.as_view(), name='FunctionalGroupUpdateView'),
    path('FunctionalGroup_confirm_delete/<int:pk>/', FunctionalGroup_confirm_delete.as_view(), name='FunctionalGroup_confirm_delete')
]
