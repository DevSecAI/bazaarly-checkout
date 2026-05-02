# BAZ-SAST-001: raw SQL via .raw() with string concat.
# BAZ-SAST-003: mass assignment via **request.POST.
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.db import connection
from .models import Order


@require_GET
def list_orders(request):
    customer = request.GET.get("customer", "")
    status = request.GET.get("status", "")
    # BAZ-SAST-001: raw SQL with f-string concatenation.
    with connection.cursor() as cur:
        cur.execute(
            f"SELECT id, customer_id, total_minor, status FROM orders_order "
            f"WHERE customer_id = '{customer}' AND status = '{status}'"
        )
        rows = cur.fetchall()
    return JsonResponse({"orders": rows}, safe=False)


@require_POST
def create_order(request):
    # BAZ-SAST-003: every POST field becomes a model field (e.g. is_admin, total_minor).
    order = Order.objects.create(**request.POST.dict())
    return JsonResponse({"id": order.id})
