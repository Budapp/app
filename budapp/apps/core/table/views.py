from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView

from budapp.helpers import url as url_helper
from budapp.apps.core.table.models import Table as TableModel

from .dynamic_form import CreateModelDocumentForm


class ListTable(ListView):
    template_name = 'table/list.html'
    model = TableModel


class DetailTable(DetailView):
    model = TableModel
    template_name = 'table/detail.html'


class CreateModelDocumentView(DetailView, FormView):
    form_class = CreateModelDocumentForm
    model = TableModel
    template_name = 'table/create_document.html'

    def get_initial(self):
        return self.kwargs

    def form_valid(self, form):
        form.create_document()

        return super().form_valid(form)

    def get_success_url(self):
        queryparams = '?msg=ok'
        return url_helper.get_url_by_name(
            'budapp_model_create_document',
            **{'pk': self.kwargs['pk']}) + queryparams

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
