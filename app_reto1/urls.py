from django.urls import path
from . import views

urlpatterns = [
    # Visualizar tickets
    path('', views.index_ticket, name='tickets'),
    path("ticket/<int:ticket_id>/", views.show_ticket, name="detalleticket"),
    # Crear tickets
    path('ticket/create', views.TicketCreateView.as_view(), name='ticket_create'),
    # Crear tickets
    path('ticket/<pk>/update', views.TicketUpdateView.as_view(),name = 'update_ticket'),

]
