from django.views.generic import ListView, DetailView
from .models import Equipo, Ticket



# PRUEBA PARA VER QUE SE VISUALIZA EN LA VENTANA
# ------------------------------------------------
from django.http import HttpResponse
def prueba(request):
    return HttpResponse("PRUEBA!")

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
