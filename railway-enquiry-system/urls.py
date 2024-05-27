from django.urls import path
from . import views

urlpatterns = [
    path('train_status/<int:train_number>/', views.train_status, name='train_status'),
    path('train_schedule/<int:train_number>/', views.train_schedule, name='train_schedule'),
    path('train_route/<int:train_number>/', views.train_route, name='train_route'),
]
