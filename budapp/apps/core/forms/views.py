from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import DetailView

from budapp.helpers import url as url_helper
from budapp.apps.core.table import models as table_models
from budapp.apps.core.table.services import table as table_service
from .dynamic_form import DynamicForm

class ModelFormView(DetailView, FormView):
    form_class = DynamicForm
    model = table_models.Table
    success_url = '/thanks/'
    template_name = 'dynamic_form/model_form/create_document.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        queryparams = '?msg=ok'
        return url_helper.get_url_by_name(
            'budapp_model_basic_form',
            **{'table_id': self.kwargs['table_id']}) + queryparams

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['table_selected'] = table_service.get_table(**self.kwargs)

        return context
