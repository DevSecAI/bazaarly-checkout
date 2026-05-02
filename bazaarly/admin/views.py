# BAZ-SAST-009: csrf_exempt on a state-changing route.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reset_pricing(request):
    # No auth check, no CSRF token. Anyone with a logged-in session
    # (or a cross-site form post) can call this.
    return JsonResponse({"ok": True})
