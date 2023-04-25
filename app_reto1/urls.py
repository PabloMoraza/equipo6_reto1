from django.urls import path
from . import views

urlpatterns = [
    # path('', views.prueba, name='prueba'),
        path('', views.EquipoListView.as_view(), name='prueba'),
        path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo'),
        path('', views.TicketListView.as_view(), name='tickets'),
        path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='ticket'),
]