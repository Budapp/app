from django.contrib import admin
from django.urls import re_path

from .views import CreateModelDocumentView

urlpatterns = [
    re_path(r'^create/(?P<pk>[\w-]+)/document/$',
            CreateModelDocumentView.as_view(),
            name='budapp_model_create_document'),
]
