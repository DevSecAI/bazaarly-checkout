# BAZ-SAST-008: SSRF via requests.get on caller-supplied URL.
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@require_POST
def callback(request):
    target = request.POST.get("callback_url", "")
    resp = requests.get(target, timeout=5)
    return JsonResponse({"status": resp.status_code})
