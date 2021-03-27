# coding: utf-8
from django.utils import translation
from django import http

from budapp.helpers import (
    user as user_helper,
    url as url_helper,
)


class BudappAuth(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (not url_helper.is_exclude_to_redirect(request) and
                not user_helper.is_authenticated(request)):
            login_url = url_helper.get_url_by_name('budapp_login')

            return http.HttpResponsePermanentRedirect(login_url)

        return response
