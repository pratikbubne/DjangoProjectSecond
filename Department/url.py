from django.urls import path
from .views import DepartmentListView, DepartmentCreateView, DepartmentUpdateView, Department_confirm_delete

urlpatterns = [
    path('DepartmentListView/', DepartmentListView.as_view(), name='DepartmentListView'),
    path('DepartmentCreateView/', DepartmentCreateView.as_view(), name='DepartmentCreateView'),
    path('DepartmentUpdateView/<int:pk>/', DepartmentUpdateView.as_view(), name='DepartmentUpdateView'),
    path('Department_confirm_delete/<int:pk>/', Department_confirm_delete.as_view(), name='Department_confirm_delete')
]
