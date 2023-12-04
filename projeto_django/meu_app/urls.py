from django.urls import path
from .views import formulario_usuario
urlpatterns = [
    path('',formulario_usuario,name=('formulario_usuario')),
]