from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
import re
from django.contrib.sites.shortcuts import get_current_site


class SubdomainMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not settings.ENV:
            parameters = request.GET.urlencode()
            if parameters:
                parameters = '?' + str(parameters)

            current_site = get_current_site(request)
            domain = current_site.domain
            pieces = domain.split('.')
            if settings.DOMAIN_MIDDLEWARE_SETTING != pieces[0]:
                current_subdomain = pieces[0]
            else:
                current_subdomain = None

            redirect_subdomain = None
            if request.user.is_authenticated:
                if request.user.firm:
                    if request.user.firm.firm_domain:
                        redirect_subdomain = request.user.firm.firm_domain
            http_protocol = 'https://'
            if redirect_subdomain and (current_subdomain != redirect_subdomain):
                if request.user.is_firm_manager:
                    return None
                else:
                    redirect_url = http_protocol + redirect_subdomain + '.' + settings.DEFAULT_SITE_DOMAIN + reverse(view_func) + parameters
                    return redirect(redirect_url)
            elif not redirect_subdomain and (current_subdomain != redirect_subdomain):
                redirect_url = http_protocol + settings.DEFAULT_SITE_DOMAIN + reverse(view_func) + parameters
                return redirect(redirect_url)
            else:
                return None
