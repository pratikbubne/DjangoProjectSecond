from django.urls import path
from .views import ProjectSiteListView, ProjectSiteDetailView, ProjectSiteCreateView, ProjectSiteUpdateView, \
    ProjectSite_confirm_delete

urlpatterns = [
    path('ProjectSiteListView/', ProjectSiteListView.as_view(), name='ProjectSiteListView'),
    path('ProjectSiteCreateView/', ProjectSiteCreateView.as_view(), name='ProjectSiteCreateView'),
    path('ProjectSiteDetailView/<int:pk>/', ProjectSiteDetailView.as_view(), name='ProjectSiteDetailView'),
    path('ProjectSiteUpdateView/<int:pk>/', ProjectSiteUpdateView.as_view(), name='ProjectSiteUpdateView'),
    path('ProjectSite_confirm_delete/<int:pk>/', ProjectSite_confirm_delete.as_view(),
         name='ProjectSite_confirm_delete')
]
