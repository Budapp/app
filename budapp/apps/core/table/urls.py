from django.contrib import admin
from django.urls import re_path, path

from .views import (
    CreateModelDocumentView,
    DetailTable,
    ListTable,
)

urlpatterns = [
    path('^list/$', ListTable.as_view(), name='budapp_list_table'),
    path('^detail/(?P<pk>[\w-]+)$', DetailTable.as_view(), name='budapp_detail_table'),
    re_path(r'^create/(?P<pk>[\w-]+)/document/$',
            CreateModelDocumentView.as_view(),
            name='budapp_model_create_document'),
]
