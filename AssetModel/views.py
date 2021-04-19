from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from AssetModel.models import AssetModel

class AssetModelCreateView(CreateView):
    model = AssetModel
    fields = ['Model_ID', 'Model_Number', 'Model_Name']

class AssetModelListView(ListView):
    model = AssetModel

class AssetModelUpdateView(UpdateView):
    model = AssetModel
    fields = ['Model_Number', 'Model_Name']

class AssetModel_confirm_delete(DeleteView):
    model = AssetModel
    success_url = reverse_lazy('AssetModelListView')
