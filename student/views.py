from django.http import HttpResponse


def index(request):
    return HttpResponse("经过了几天的努力，一切终于正常啦")