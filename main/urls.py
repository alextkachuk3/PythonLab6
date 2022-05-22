from . import views
from django.urls import path

urlpatterns = [
    path('', views.metro, name='stations-list'),
]
