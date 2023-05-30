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
    # Visualizar empleados
    path('empleados/', views.index_empleados, name='empleados'),
    path("empleados/<int:empleado_id>/", views.show_empleado, name="detalleempleado"),
    # Crear empleados
    path('empleados/create', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    # Editar empleados
    path('empleados/<pk>/update', views.EmpleadoUpdateView.as_view(),name = 'empleado_update'),
    #Borrar empleados
    path('empleados/<pk>/delete', views.EmpleadoDeleteView.as_view(), name= 'empleado_delete'),
    # Visualizar proveedores
     path('proveedores/', views.index_proveedores, name='proveedores'),
    path("proveedores/<int:proveedor_id>/", views.show_proveedor, name="detalleproveedor"),
    path('proveedores_api/', views.ProveedorListView.as_view(), name='proveedores_api'),
    # path("proveedores_api/<int:pk>/", views.ProveedorDetailView.as_view(), name="detalleproveedor_api"),
    # Crear proveedores
    path('proveedores/create', views.ProveedorCreateView.as_view(), name='proveedor_create'),
    # Editar proveedores
    path('proveedores/<pk>/update', views.ProveedorUpdateView.as_view(),name = 'proveedor_update'),
    #Borrar proveedores
    path('proveedores/<pk>/delete', views.ProveedorDeleteView.as_view(), name= 'proveedor_delete'),
    # tickets de un empleado
    path('empleados/<int:empleado_id>/tickets',views.tickets_de_empleado, name = "tickets_de_empleado"),
    # tickets de un equipo
    path('equipos/<int:equipo_id>/tickets', views.tickets_de_equipo, name = "tickets_de_equipo" ),
    # equipos de un proveedor
    path('proveedores/<int:proveedor_id>/equipos', views.equipos_de_proveedor, name = "equipos_de_proveedor" ),

]
