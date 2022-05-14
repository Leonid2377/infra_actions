from django.http import HttpResponse

from http import HTTPStatus


def index(request):
    return HTTPStatus.OK, HttpResponse('У меня получилось!')


def second_page(request):
    return HTTPStatus.OK, HttpResponse('А это вторая страница')
