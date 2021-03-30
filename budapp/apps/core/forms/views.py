from django.shortcuts import render
from django.views.generic.edit import FormView

from budapp.helpers import url as url_helper

from .dynamic_form import DynamicForm


class ModelFormView(FormView):
    template_name = 'dynamic_form/model_form.html'
    form_class = DynamicForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        queryparams = '?msg=ok'
        return url_helper.get_url_by_name(
            'budapp_model_basic_form',
            **{'table_id': self.kwargs['table_id']}) + queryparams
