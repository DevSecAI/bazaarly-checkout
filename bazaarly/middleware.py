# BAZ-SAST-011: full traceback returned in error response (paired with DEBUG=True).
import traceback
from django.http import JsonResponse


class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:
            return JsonResponse(
                {"error": str(e), "trace": traceback.format_exc()},
                status=500,
            )
