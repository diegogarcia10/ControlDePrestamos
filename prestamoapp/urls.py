from django.conf.urls import url, include
from apps.prestamoapp.views import misArticulos,probando,ListArticuloView

app_name="prestamoapp"
urlpatterns = [
 
    url(r'nuevo',misArticulos, name='prestamo_articulo'),
    url(r'prueba',probando, name='prueba'),
    url(r'artic',ListArticuloView.as_view(),name='articulo_list')
]