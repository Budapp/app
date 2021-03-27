from django.contrib import admin
from django.urls import re_path

from .views import LoginView

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(), name='budapp_login'),
]
