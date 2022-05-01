from django.forms import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Car, Category
from .forms import CarSearchForm

host = 'http://127.0.0.1:8000/'

def home_page(request):
    return render(request, 'cars/home_page.html')

class CarDetailView(DetailView):
    model = Car


class CarListView(ListView):
    paginate_by = 20
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = CarSearchForm(self.request.GET)
        return context

    #
    def get_queryset(self):
        qs = super().get_queryset()

        form = CarSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            category_id = form.cleaned_data['category']

            if name:
                qs = qs.filter(name__icontains=name)

            if year:
                qs = qs.filter(year=year)

            if category_id:
                qs = qs.filter(category_id=category_id)

        return qs

class CarCreateView(CreateView):
    model = Car
    fields = ['name','price', 'currency', 'year','category']
    success_url = host

class CarUpdateView(UpdateView):
    model = Car
    fields = ['name', 'price', 'currency', 'year', 'category']
    success_url = host

class CarDeleteView(DeleteView):
    model = Car
    success_url = host