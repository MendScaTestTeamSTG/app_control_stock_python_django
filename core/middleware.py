from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class BlockTrailingNewlineMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.endswith('\n'):
            return HttpResponseBadRequest("Request URL contains invalid characters.")
