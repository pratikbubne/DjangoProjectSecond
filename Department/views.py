from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from Department.models import Department
from django.urls import reverse_lazy

# Create your views here.
class DepartmentListView(ListView):
    model = Department

class DepartmentCreateView(CreateView):
    model = Department
    fields = ['Dept_ID', 'Dept_Name']

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['Dept_ID', 'Dept_Name']

class Department_confirm_delete(DeleteView):
    model = Department
    success_url = reverse_lazy('DepartmentListView')
