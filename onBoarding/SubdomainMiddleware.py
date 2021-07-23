from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
import re
from django.contrib.sites.shortcuts import get_current_site


class SubdomainMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        parameters = request.GET.urlencode()
        if parameters:
            parameters = '?' + str(parameters)

        current_site = get_current_site(request)
        domain = current_site.domain
        pieces = domain.split('.')
        if settings.DEFAULT_SITE_DOMAIN != pieces[0]:
            current_subdomain = pieces[0]
        else:
            current_subdomain = None

        redirect_subdomain = None
        if request.user.is_authenticated:
            if request.user.firm:
                if request.user.firm.firm_domain:
                    redirect_subdomain = request.user.firm.firm_domain

        if request.is_secure():
            first_part = 'https://'
        else:
            first_part = 'http://'

        print("redirect_subdomain", redirect_subdomain)
        print("SESSION_COOKIE_NAME:", settings.SESSION_COOKIE_NAME)
        print("SESSION_COOKIE_DOMAIN:", settings.SESSION_COOKIE_DOMAIN)

        # if redirect_subdomain and current_subdomain != redirect_subdomain:
        #     # print('1' * 40)
        #     redirect_url = first_part + redirect_subdomain + '.' + settings.DEFAULT_SITE_DOMAIN + reverse(view_func) + parameters
        #     return redirect(redirect_url)
        # elif not redirect_subdomain and current_subdomain != redirect_subdomain:
        #     print('2' * 40)
        #     redirect_url = first_part + settings.DEFAULT_SITE_DOMAIN + reverse(view_func) + parameters
        #     return redirect(redirect_url)
        # else:
        #     # print('3' * 40)
        #     return None


class CrossDomainSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.cookies:
            host = request.get_host()
            # check if it's a different domain
            if host not in settings.SESSION_COOKIE_DOMAIN:
                domain = ".{domain}".format(domain=host)
                print("domain:", domain)
                for cookie in response.cookies:
                    if 'domain' in response.cookies[cookie]:
                        response.cookies[cookie]['domain'] = domain
        return response

# class SubdomainMiddleware(object):
#     """Middleware class that redirects non "www" subdomain requests to a
#     specified URL or business.
#     """
#     def process_request(self, request):
#         """Returns an HTTP redirect response for requests including non-"www"
#         subdomains.
#         """
#         scheme = "http" if not request.is_secure() else "https"
#         path = request.get_full_path()
#         domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
#         pieces = domain.split('.')
#         subdomain = ".".join(pieces[:-2]) # join all but primary domain
#         default_domain = 'test'
#         # if domain in {default_domain, "testserver", "localhost"}:
#         #     return None
#         # try:
#         route = 'test'
#         # except Subdomain.DoesNotExist:
#         #     route = path
#         return HttpResponseRedirect("{0}://{1}{2}".format(scheme, default_domain, route))
