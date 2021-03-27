from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from budapp.apps.authentication.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    success_url = ('budapp_home_page')
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
        form.login(self.request)
        return super(LoginView, self).form_valid(form)
