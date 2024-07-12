from django.urls import path 
from . import views



urlpatterns = [
    path('index', views.mostrar_index, name='index'),
    path('sesion', views.mostrar_sesion, name='sesion'),
    path('registrarse', views.mostrar_registrarse, name='registrarse'),
    path('nostros', views.mostrar_nosotros, name='nostros'),
    path('jardineria', views.mostrar_jardineria, name='jardineria'),
    path('herramientas', views.mostrar_herramientas, name='herramientas'),
    path('carrito', views.mostrar_carrito, name='carrito'),
    
]