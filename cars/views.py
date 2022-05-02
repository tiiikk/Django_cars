from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.forms import models
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from car import settings
from .models import Car, Category
from .forms import CarSearchForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views, authenticate, login, logout

host = 'http://127.0.0.1:8000/car/all/'

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         return render(request,'registration/login.html')


@login_required(login_url='/registration/login/')


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