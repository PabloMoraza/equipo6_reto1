from django.views.generic import ListView, DetailView
from .models import Ticket, Urgencia, Tipo_ticket, Estado_ticket, Empleado
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
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

# listado tickets basico


def index_ticket(request):
    tickets = get_list_or_404(Ticket.objects.order_by("num_referencia"))
    context = {"lista_tickets" : tickets}
    return render(request, "ticket_lista.html", context)


# datos de un ticket basico
def show_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {"ticket" : ticket}
    return render(request, "ticket_descripcion.html", context)


# ticket por urgencia
def index_ticket_x_urgencias(request, urgencia_id):
    urgencia = get_object_or_404(Urgencia, pk=urgencia_id)
    tickets = urgencia.ticket_set.all()
    context = {"urgencia" : urgencia, "tickets" : tickets }
    return render(request, "detail.html", context)

# # ticket por tipo


# def index_ticket_x_tipo(request, tipo_id):
#     tipo = get_object_or_404(Tipo_ticket, pk=tipo_id)
#     tickets = tipo.ticket_set.all()
#     context = {"tipo" : tipo, "tickets" : tickets }
#     return render(request, "detail.html", context)

# # ticket por empleado


# def index_ticket_x_empleado(request, empleado_id):
#     empleado = get_object_or_404(Empleado, pk=empleado_id)
#     output = ", ".join(
#         [f"{e.num_referencia} {e.equipo_a_reparar}" for e in empleado.ticket_set.all()])
#     return HttpResponse(output)

# # ticket por estado


# def index_ticket_x_estado(request, estado_id):
#     estado = get_object_or_404(Estado_ticket, pk=estado_id)
#     output = ", ".join(
#         [f"{e.num_referencia} {e.equipo_a_reparar}" for e in estado.ticket_set.all()])
#     return HttpResponse(output)
