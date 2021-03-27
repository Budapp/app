from django.contrib import admin
from django.urls import path

from .views import HomeView

urlpatterns = [
    path(r'', HomeView.as_view(), name='budapp_home_page'),
]
