from django.urls import path
from . import views

urlpatterns = [
    path('', views.prueba, name='prueba'),
    # path('', views.EquipoListView.as_view(), name='equipos'),
]