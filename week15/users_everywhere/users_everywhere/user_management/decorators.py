from django.shortcuts import redirect
from functools import wraps

# ako veche sum se lognal(ako v sesiqta imam takuv email,
# ne me prashtai na login,
# a me preprati na /profile


def login_required(redirect_url=None):
    if redirect_url is None:
        redirect_url = '/'

    def decorator(func):

        @wraps(func)
        def _wrapped_view(request, *args, **kwargs):
            session_email = request.session.get('email', False)

            if not session_email:
                return redirect(redirect_url)

            return func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def annon_required(redirect_url=None):
    if redirect_url is None:
        redirect_url = '/'

    def decorator(func):

        @wraps(func)
        def _wrapped_view(request, *args, **kwargs):
            session_email = request.session.get('email', False)

            if session_email:
                return redirect(redirect_url)

            return func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


