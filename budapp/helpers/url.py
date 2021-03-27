from django.urls import reverse
from django.shortcuts import redirect


def get_url_by_name(url_name, **kwags):
    try:
        url = reverse(url_name, kwargs=kwags)
    except:
        url = None
    finally:
        return url


def is_current_page_login(request):
    return request.path == get_url_by_name('budapp_login')


def is_exclude_to_redirect(request):
    return (
        'admin' in request.path or
        is_current_page_login(request))


def redirect_to(url_name):
    url = get_url_by_name(url_name)

    return redirect(url)
