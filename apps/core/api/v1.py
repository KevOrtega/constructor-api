from django.http import HttpResponse

def get_v1(request):
    return HttpResponse(True)