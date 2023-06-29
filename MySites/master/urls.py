from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='master-home'),
    path('about/', views.about, name='master-about'),
]
