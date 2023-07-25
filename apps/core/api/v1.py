from django.http import HttpResponse


def get_livez(request):
    return HttpResponse(True)
