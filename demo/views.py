from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Demo
from .forms import DemoForm


class DemoListView(ListView):
    model = Demo
    # template_name = 'demo/list.html'
    template_name = 'demo/list.html'


class DemoCreateView(CreateView):
    model = Demo
    form_class = DemoForm
    template_name = 'demo/edit.html'


class DemoDetailView(DetailView):
    model = Demo
    template_name = 'demo/detail.html'


class DemoUpdateView(UpdateView):
    model = Demo
    form_class = DemoForm
    template_name = 'demo/edit.html'


class DemoDeleteView(DeleteView):
    model = Demo
    form_class = DemoForm
    template_name = 'demo/delete.html'
    success_url = reverse_lazy('demo:list')
