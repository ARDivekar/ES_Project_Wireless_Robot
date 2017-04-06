from django.shortcuts import render

# Create your views here.


## The following was created by Abhishek Divekar, 6th Apr 2017
from django.http import HttpResponse

from get_sensor_data import *

def index(request):
    #return render(request, 'controls/controls.html', {})
    return HttpResponse(str(current_ir_sensor_data()))

