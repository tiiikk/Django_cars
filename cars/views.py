from django.forms import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Car, Category
from .forms import CarSearchForm


class CarDetailView(DetailView):
    model = Car


class CarListView(ListView):
    paginate_by = 10
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = CarSearchForm(self.request.GET)
        return context

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


class CarMixin:
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('cars:car_list')


class CarCreateView(CarMixin, CreateView):
    fields = ('name', 'vin', 'price', 'currency', 'category', 'year', 'image')

    # def get(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseRedirect('/')
    #     return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CarUpdateView(CarMixin, UpdateView):
    fields = ('name', 'vin', 'price', 'currency', 'category', 'year', 'image')

    def get_queryset(self):
        # qs = super().get_queryset()
        # qs = qs.filter(author_id=self.request.user.pk)
        # return qs
        return Car.objects.filter(author_id=self.request.user.pk)


class CarDeleteView(CarMixin, DeleteView):
    pass

    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save()

    # def get(self, request, *args, **kwargs):
    #     obj = super().get(request, *args, **kwargs)
    #     if self.object.author_id != self.request.user.pk:
    #         return HttpResponseRedirect('/')
    #     return obj

    def get_queryset(self):
        # qs = super().get_queryset()
        # qs = qs.filter(author_id=self.request.user.pk)
        # return qs
        return Car.objects.filter(author_id=self.request.user.pk)
