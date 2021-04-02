from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import DetailView

from budapp.helpers import url as url_helper
from budapp.apps.core.table.models import Table as TableModel

from .dynamic_form import CreateModelDocumentForm


class CreateModelDocumentView(DetailView, FormView):
    form_class = CreateModelDocumentForm
    model = TableModel
    template_name = 'table/create_document.html'

    def get_initial(self):
        return self.kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        queryparams = '?msg=ok'
        return url_helper.get_url_by_name(
            'budapp_model_create_document') + queryparams
