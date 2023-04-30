from django.urls import path
from . import views

urlpatterns = [
    # Visualizar tickets
    path('', views.index_ticket, name='tickets'),
    path("ticket/<int:ticket_id>/", views.show_ticket, name="detalleticket"),
    # Crear tickets
    path('ticket/create', views.TicketCreateView.as_view(), name='ticket_create'),
    # Editar tickets
    path('ticket/<pk>/update', views.TicketUpdateView.as_view(),name = 'update_ticket'),
    #Borrar tickets
    path('ticket/<pk>/delete', views.TicketDeleteView.as_view(), name= 'delete_ticket'),
    # Visualizar equipos
    path('equipos/', views.index_equpos, name='equipos'),
    path("equipos/<int:equipo_id>/", views.show_equipo, name="detalleequipo"),
    # Crear equipos
    path('equipos/create', views.EquipoCreateView.as_view(), name='equipo_create'),
    # Editar equipos
    path('equipos/<pk>/update', views.EquipoUpdateView.as_view(),name = 'update_equipo'),
    #Borrar tickets
    path('equipos/<pk>/delete', views.EquipoDeleteView.as_view(), name= 'delete_equipo'),

]
