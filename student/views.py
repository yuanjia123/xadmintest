from django.http import HttpResponse


def index(request):
    return HttpResponse("第一个视图")