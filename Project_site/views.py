from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from Project_site.models import ProjectSite
from django.urls import reverse_lazy

# Create your views here.
class ProjectSiteListView(ListView):
    model = ProjectSite

class ProjectSiteCreateView(CreateView):
    model = ProjectSite
    fields = ['Site_ID', 'Site_Name', 'Site_Location', 'Site_Department', 'Site_Code', 'Organization_ID', 'Organization_Name']

class ProjectSiteDetailView(DetailView):
    model = ProjectSite
    template_name = "Project_site/Projectsite_detail.html"

class ProjectSiteUpdateView(UpdateView):
    model = ProjectSite
    fields = ['Site_Name', 'Site_Location', 'Site_Department', 'Site_Code', 'Organization_ID', 'Organization_Name']

class ProjectSite_confirm_delete(DeleteView):
    model = ProjectSite
    success_url = reverse_lazy('ProjectSiteListView')
