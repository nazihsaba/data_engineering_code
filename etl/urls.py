from django.urls import path
from . import views

urlpatterns = [
    path('client_summary/', views.client_summary, name='client_summary'),
    path('register/', views.register, name='register'),
]