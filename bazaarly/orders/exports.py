# BAZ-SAST-007: path traversal in /orders/export/<filename>.
import os
from django.http import FileResponse, HttpResponseNotFound

EXPORT_ROOT = "/var/bazaarly/exports"


def export(request, filename):
    # BAZ-SAST-007: filename is interpolated without normalisation.
    target = os.path.join(EXPORT_ROOT, filename)
    if not os.path.exists(target):
        return HttpResponseNotFound()
    return FileResponse(open(target, "rb"))
