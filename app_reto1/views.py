from django.views.generic import ListView, DetailView
from .models import Ticket, Urgencia
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
    ticket = Ticket.objects.order_by("num_referencia")
    output = ", ".join(
        [f"{e.num_referencia}  {e.equipo_a_reparar}" for e in ticket])
    return HttpResponse(output)
# Prueba martin datos de un ticket


def show_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    output = f"{ticket.num_referencia}: {ticket.equipo_a_reparar}, {ticket.descripcion} {ticket.detalles} {ticket.fecha_apertura} {ticket.fecha_resolucion} {ticket.urgencia} {ticket.tipo_ticket} {ticket.estado_ticket} {ticket.empleado_asignado} {ticket.comentarios_ticket} "
    return HttpResponse(output)
 # Prueba martin ticket por urgencia
def index_ticket_x_urgencias(request, urgencia_id):
    urgencia = Urgencia.objects.get(pk=urgencia_id)
    output = ", ".join([f"{e.num_referencia} {e.equipo_a_reparar}" for e in urgencia.ticket_set.all()])
    return HttpResponse(output)
