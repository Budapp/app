from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('forms/', include('budapp.apps.core.forms.urls')),
    path('table/', include('budapp.apps.core.table.urls')),
]
