from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_ticket, name='tickets'),
    path("ticket/<int:ticket_id>/", views.show_ticket, name="detalleticket"),
    path('ticket/create', views.TicketCreateView.as_view(), name='ticket_create'),

]
