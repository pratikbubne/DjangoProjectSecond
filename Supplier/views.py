from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from Supplier.models import Supplier
from django.urls import reverse_lazy

class SupplierCreateView(CreateView):
    model = Supplier
    fields = ['Supplier_Name', 'Supplier_Mailid', 'Supplier_Mobile', 'City', 'Address']

class SupplierListView(ListView):
    model = Supplier

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "Supplier/Supplier_details.html"

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = ['Supplier_Name', 'Supplier_Mailid', 'Supplier_Mobile', 'City', 'Address']

class Supplier_confirm_delete(DeleteView):
    model = Supplier
    success_url = reverse_lazy('SupplierListView')

