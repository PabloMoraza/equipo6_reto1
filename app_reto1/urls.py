from django.urls import path
from . import views

# urlpatterns = [
#     # path('', views.prueba, name='prueba'),
#     path('', views.EquipoListView.as_view(), name='equipos'),
# ]

urlpatterns = [
     path('', views.index_empleados, name ='empleados'),
     path('empleados/<int:empleado_id>/', views.show_empleados, name = "detalle empleado" ),
     path('plantas/<int:planta_id>/equipos',views.index_equipos_por_planta, name = "equiposxplanta")
]