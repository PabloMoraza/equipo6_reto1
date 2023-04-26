from django.views.generic import ListView, DetailView
from .models import Empleado, Planta, Equipo
from django.http import HttpResponse
# from .models import Equipo, Ticket

# # PRUEBA PARA VER QUE SE VISUALIZA EN LA VENTANA
# # ------------------------------------------------
# from django.http import HttpResponse
# def prueba(request):
#     return HttpResponse("PRUEBA!")

# # ----------------------------------------------------
# # VISTAS DE EQUIPO
# class EquipoListView(ListView):
#     model = Equipo

# class EquipoDetailView(DetailView):
#    model = Equipo
# # ------------------------------------------------------
# # # ----------------------------------------------------
# # VISTAS DE TICKET
# class TicketListView(ListView):
#     model = Ticket

# class TicketDetailView(DetailView):
#    model = Ticket
# # ------------------------------------------------------

# Prueba martin listado empleados
def index_empleados(request):
    empleados = Empleado.objects.order_by("apellido1")
    output = ", ".join([d.apellido1 for d in empleados])
    return HttpResponse(output)
# Prueba martin datos de un empleado
def show_empleados(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    output = f'{empleado.apellido1} {empleado.apellido2}, {empleado.nombre} DNI: {empleado.DNI} Contacto: {empleado.email} {empleado.telefono}'
    return HttpResponse(output)
# Prueba martin equipos por planta
def index_equipos_por_planta(request, planta_id):
    planta = Planta.objects.get(pk=planta_id)
    output = ", ".join([f"{e.num_serie} {e.marca} {e.modelo}" for e in planta.equipo_set.all()])
    # output = ", ".join(["{e.num_serie} {e.marca} {e.modelo}" for e in planta.equipo_set.all()])
    return HttpResponse(output)
