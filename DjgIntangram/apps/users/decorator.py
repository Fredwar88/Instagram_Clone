from django.http import HttpResponse
from django.shortcuts import redirect

def auth_user_restriction(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('posts:feed')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func