from django.views.generic import ListView, DetailView
from .models import Ticket, Urgencia, Tipo_ticket, Estado_ticket, Empleado
from django.shortcuts import get_list_or_404, get_object_or_404
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

# Prueba  listado tickets


def index_ticket(request):
    ticket = get_list_or_404(Ticket.objects.order_by("num_referencia"))
    output = ", ".join([f"{e.num_referencia}  {e.equipo_a_reparar}" for e in ticket])
    return HttpResponse(output)
# Prueba martin datos de un ticket


def show_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    output = f"{ticket.num_referencia}: {ticket.equipo_a_reparar}, {ticket.descripcion} {ticket.detalles} {ticket.fecha_apertura} {ticket.fecha_resolucion} {ticket.urgencia} {ticket.tipo_ticket} {ticket.estado_ticket} {ticket.empleado_asignado} {ticket.comentarios_ticket} "
    return HttpResponse(output)
 # Prueba martin ticket por urgencia


def index_ticket_x_urgencias(request, urgencia_id):
    urgencia = get_object_or_404(Urgencia, pk=urgencia_id)
    output = ", ".join(
        [f"{e.num_referencia} {e.equipo_a_reparar}" for e in urgencia.ticket_set.all()])
    return HttpResponse(output)

def index_ticket_x_tipo(request, tipo_id):
    tipo = get_object_or_404(Tipo_ticket, pk=tipo_id)
    output = ", ".join(
        [f"{e.num_referencia} {e.equipo_a_reparar}" for e in tipo.ticket_set.all()])
    return HttpResponse(output)

def index_ticket_x_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    output = ", ".join(
        [f"{e.num_referencia} {e.equipo_a_reparar}" for e in empleado.ticket_set.all()])
    return HttpResponse(output)

def index_ticket_x_estado(request, estado_id):
    estado = get_object_or_404(Estado_ticket, pk=estado_id)
    output = ", ".join(
        [f"{e.num_referencia} {e.equipo_a_reparar}" for e in estado.ticket_set.all()])
    return HttpResponse(output)