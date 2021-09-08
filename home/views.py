from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import socket

# Create your views here.

def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response = HttpResponse()
    response.writelines('<h1>Hello ' + ip + '</h1>')
    response.writelines('<h2>Current time ' + current_time )
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    response.writelines('<h2>Current IP ' + local_ip )
    return response
