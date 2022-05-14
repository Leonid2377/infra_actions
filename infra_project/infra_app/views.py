from http import HTTPStatus

from django.http import HttpResponse


def index(request):
    return HttpResponse(HTTPStatus.OK, 'У меня получилось!')


def second_page(request):
    return HttpResponse(HTTPStatus.OK, 'А это вторая страница')
