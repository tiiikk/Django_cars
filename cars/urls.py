from django.urls import path

from cars.views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, home_page

app_name = 'cars'
urlpatterns = [
    path('help/', home_page, name='home_page'),
    path('all/', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('add/', CarCreateView.as_view(), name='car_form'),
    path('update/<int:pk>', CarUpdateView.as_view(), name='car_form'),
    path('delete/<int:pk>', CarDeleteView.as_view(), name='car_delete'),
]