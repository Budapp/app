from django.contrib.auth import authenticate, login

from budapp.helpers import url as url_helper


def authenticate_user(email, password, request):
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)

    return user
