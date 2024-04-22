from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from accounts.views import login_view, logout_view, register_view
from app import settings
from django.conf.urls.static import static
from cars.views import (
    CarDeleteView, CarDetailView, CarUpdateView, CarsListView, NewCarCreateView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', lambda request: redirect('/cars')),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
