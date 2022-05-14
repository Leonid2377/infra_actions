from http import HTTPStatus

from django.http import HttpResponse


def index(request):
    return HTTPStatus.OK, HttpResponse('У меня получилось!')


def second_page(request):
    return HTTPStatus.OK, HttpResponse('А это вторая страница')
