from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

app_name = 'cars'
urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>/detail/', CarDetailView.as_view(), name='car_detail'),
    path('create/', login_required(CarCreateView.as_view()), name='car_create'),
    path('<int:pk>/update/', login_required(CarUpdateView.as_view()), name='car_update'),
    path('<int:pk>/delete/', login_required(CarDeleteView.as_view()), name='car_delete'),
]
