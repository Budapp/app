from django.contrib import admin
from django.urls import re_path

from .views import ModelFormView

urlpatterns = [
    re_path(r'^model-form/(?P<table_id>[\w-]+)/$',
            ModelFormView.as_view(),
            name='budapp_model_basic_form'),
]
