from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from Functional_group.models import FunctionalGroup
from django.urls import reverse_lazy

# Create your views here.
class FunctionalGroupListView(ListView):
    model = FunctionalGroup

class FunctionalGroupCreateView(CreateView):
    model = FunctionalGroup
    fields = ['Fun_ID', 'Functional_Group']

class FunctionalGroupUpdateView(UpdateView):
    model = FunctionalGroup
    fields = ['Functional_Group']

class FunctionalGroup_confirm_delete(DeleteView):
    model = FunctionalGroup
    success_url = reverse_lazy('FunctionalGroupListView')
