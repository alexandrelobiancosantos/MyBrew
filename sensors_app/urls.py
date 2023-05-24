from django.urls import include, path

from sensors_app.views import dashboard, dht11_data, dht11_graph, index

urlpatterns = [
    path('', index, name='index'),
    path('dht11_data/', dht11_data, name='dht11_data'),
    path('dht11_graph/', dht11_graph, name='dht11_graph'),
    path('dashboard/', dashboard, name='dashboard'),
]
