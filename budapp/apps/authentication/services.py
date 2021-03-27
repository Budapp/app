from django.contrib.auth import login
from django.contrib.auth.models import User

from budapp.helpers import url as url_helper


def authenticate_user(email, password, request):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None
    else:
        if not user.check_password(password):
            user = None

    if user is not None:
        login(request, user)

    return user
