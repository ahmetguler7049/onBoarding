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
                print("USER IS AUTHENTICATED")
                if request.user.firm:
                    print("USER HAS GOT A FIRM")
                    if request.user.firm.firm_domain:
                        print("USER HAS GOT A FIRM_DOMAIN")
                        redirect_subdomain = request.user.firm.firm_domain

            if request.is_secure():
                http_protocol = 'https://'
            else:
                http_protocol = 'http://'
            http_protocol = 'https://'
            print("redirect_subdomain:", redirect_subdomain)
            print("current_subdomain:", current_subdomain)
            if redirect_subdomain and (current_subdomain != redirect_subdomain):
                redirect_url = http_protocol + redirect_subdomain + '.' + settings.DEFAULT_SITE_DOMAIN + reverse(view_func) + parameters
                print(redirect_url)
                return redirect(redirect_url)
            elif not redirect_subdomain and (current_subdomain != redirect_subdomain):
                redirect_url = http_protocol + settings.DEFAULT_SITE_DOMAIN + reverse(view_func) + parameters
                print(redirect_url)
                return redirect(redirect_url)
            else:
                print("NOTHING HAPPENED!")
                return None
