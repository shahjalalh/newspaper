from django.http import HttpResponse


def healthcheck(request):
    """Health check view, returns a empty HTTP 200 response."""
    return HttpResponse()
