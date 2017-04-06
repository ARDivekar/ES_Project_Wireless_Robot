from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'controls/controls.html', {})
    #return HttpResponse("Hello, world. You're at the controls index page.")

from MazeSolver.rc_car import *



def controls(request, direction):
    #return HttpResponse("Control: %s"%(direction))
    if direction.lower()=="forward":
        forward()
    elif direction.lower()=="backward":
        backward()
    elif direction.lower()=="left":
        left()
    elif direction.lower()=="right":
        right()
    elif direction.lower()=="stop":
        stop()
    return render(request, 'controls/controls.html', {"direction": direction})

