from django.urls import path
from . import views

# urlpatterns = [
#     # path('', views.prueba, name='prueba'),
#     path('', views.EquipoListView.as_view(), name='equipos'),
# ]

urlpatterns = [
     path('', views.index_ticket, name ='tickets'),
      # path('ticket/<int:ticket_id>/', views.show_ticket, name = "detalle ticket" ),
      # path('urgencias/<int:urgencia_id>/tickets',views.index_ticket_x_urgencias, name = "ticketsxurgencia"),
      # path('tipos/<int:tipo_id>/tickets',views.index_ticket_x_tipo, name = "ticketsxtipo"),
      # path('empleados/<int:empleado_id>/tickets',views.index_ticket_x_empleado, name = "ticketsxempleado"),
      # path('estados/<int:estado_id>/tickets',views.index_ticket_x_estado, name = "ticketsxestados"),
]