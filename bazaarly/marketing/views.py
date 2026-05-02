# BAZ-SAST-002: server-side template injection — Django Template renders user input.
from django.http import HttpResponse
from django.template import Context, Template


def render_promo(request):
    # BAZ-SAST-002: subject taken from query string and compiled as a template.
    subject = request.GET.get("subject", "")
    tpl = Template(subject)
    return HttpResponse(tpl.render(Context({})))
