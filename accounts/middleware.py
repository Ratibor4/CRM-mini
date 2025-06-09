from django.http import HttpResponseForbidden
from django.conf import settings

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(f'/{settings.ADMIN_URL}'):
            if not request.user.is_authenticated or not request.user.is_admin_account:
                return HttpResponseForbidden("Доступ запрещен")
        return self.get_response(request)