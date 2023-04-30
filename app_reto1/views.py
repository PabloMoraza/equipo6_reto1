from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
from .models import Ticket, Urgencia, Tipo_ticket, Estado_ticket, Empleado
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from app_reto1.forms import TicketForm


# Lista de tickets
def index_ticket(request):
    tickets = get_list_or_404(Ticket.objects.order_by("fecha_apertura"))
    context = {"lista_tickets": tickets}
    return render(request, "ticket_list.html", context)

# datos de un ticket


def show_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {"ticket": ticket}
    return render(request, "ticket_descripcion.html", context)

# Crear ticket


class TicketCreateView(View):
    # Llamada para mostrar la página con el formulario de creación
    def get(self, request, *args, **kwargs):
        formulario = TicketForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'Ticket_create.html', context)

    # Llamada para procesar la creación del ticket
    def post(self, request, *args, **kwargs):
        formulario = TicketForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            # Volvemos a la lista de ticket
            return redirect('tickets')

        return render(request, 'Ticket_create.html', {'formulario': formulario})
    
class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = "ticket_update.html"
    success_url = "/aplicacion/"
    fields = ['equipo_a_reparar', 'num_referencia', 'descripcion', 'detalles', 'fecha_apertura', 'fecha_resolucion', 'urgencia', 'tipo_ticket', 'estado_ticket','empleado_asignado','comentarios_ticket']

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name ="delete.html"
    success_url = "/aplicacion/"

    

