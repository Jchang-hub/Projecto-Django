from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('consulta', views.consulta, name='consulta'),
    path('nuevo', views.nuevo, name='nuevo'),
    path('consulta/<int:id>', views.consulta, name='consulta'),  
    path('json', views.json, name='json'), 
    path('consulta/json', views.json, name='json'),   
]