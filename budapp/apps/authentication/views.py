from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from budapp.apps.authentication.forms import LoginForm
from budapp.helpers import url as url_helper


class LoginView(FormView):
    form_class = LoginForm
    success_url = url_helper.get_url_by_name('budapp_home_page')
    template_name = 'login.html'

    def get_form_kwargs(self):
        kw = super(LoginView, self).get_form_kwargs()
        kw['request'] = self.request

        return kw

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)
