from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hw04/', views.hw04_view, name='hw04'),
]