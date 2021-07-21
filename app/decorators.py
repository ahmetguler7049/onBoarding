from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site


def subdomain_adjuster(view_func):
    def wrapper(request, *args, **kwargs):
        domain = get_current_site(request).domain
        return view_func(request, *args, **kwargs)

    return wrapper
