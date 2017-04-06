from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("""<html><head></head><body><h1>Hello, world. You're at the view_count index page.</h1></body></html>""")
