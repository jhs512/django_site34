from django.http import HttpResponse, HttpRequest
from django.urls import path

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("테스트 A")


def index2(request: HttpRequest) -> HttpResponse:
    return HttpResponse("테스트 B")


urlpatterns = [
    path('a', index),
    path('b', index2),
]
