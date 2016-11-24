from django.http import HttpResponse

def index(request):
    return HttpResponse("Travel Calendar Parser")
