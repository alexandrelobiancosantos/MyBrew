# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'sensors_app/pages/index.html', context={
        'temperature_sensor_id': 'DHT11_1',
        'humidity_sensor_id': 'DHT11_1',
    })


def dht11_graph(request):
    return HttpResponse("<div style='display: flex; align-items: center; justify-content: center; position: absolute; top: 0; bottom: 0; left: 0; right: 0;'><h1>Hello, world. <br>You're at the dht11 graph page.</h1></div>")


def dht11_data(request):
    return HttpResponse("<div style='display: flex; align-items: center; justify-content: center; position: absolute; top: 0; bottom: 0; left: 0; right: 0;'><h1>Hello, world.<br> You're at the dht11 data page.</h1></div>")


def dashboard(request):
    return HttpResponse("<div style='display: flex; align-items: center; justify-content: center; position: absolute; top: 0; bottom: 0; left: 0; right: 0;'><h1>Hello, world.<br> You're at the dht11 dashboard.</h1></div>")
