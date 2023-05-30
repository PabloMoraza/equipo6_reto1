from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Ticket, Empleado, Equipo, Proveedor
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from app_reto1.forms import TicketForm, EquipoForm, EmpleadoForm, ProveedorForm
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.forms.models import model_to_dict

# Lista de tickets


def index_ticket(request):
    busqueda = request.GET.get("buscar")
    tickets = get_list_or_404(Ticket.objects.order_by("fecha_apertura"))
    page = request.GET.get("page", 1)

    try:
        paginator = Paginator(tickets, 4)
        tickets = paginator.page(page)
    except:
        raise Http404

    if busqueda:
        tickets = Ticket.objects.filter(
            Q(num_referencia__icontains=busqueda) |
            Q(fecha_apertura__icontains=busqueda) |
            Q(urgencia__gravedad__icontains=busqueda) |
            Q(estado_ticket__estado__icontains=busqueda) |
            Q(equipo_a_reparar__modelo__icontains=busqueda) |
            Q(empleado_asignado__DNI__icontains=busqueda) |
            Q(tipo_ticket__tipo__icontains=busqueda)
        ).distinct()
    data = {
        "lista_tickets": tickets,
        "paginator": paginator
    }

    return render(request, "ticket_list.html", data)

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

    # Modificar ticket


class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = "ticket_update.html"
    success_url = "/aplicacion/"
    fields = ['equipo_a_reparar', 'num_referencia', 'descripcion', 'detalles', 'fecha_apertura',
              'fecha_resolucion', 'urgencia', 'tipo_ticket', 'estado_ticket', 'empleado_asignado', 'comentarios_ticket']


# borrar ticket

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = "delete.html"
    success_url = "/aplicacion/"

# Lista de Equipos


def index_equpos(request):
    busqueda = request.GET.get("buscar")
    equipos = get_list_or_404(Equipo.objects.order_by("num_serie"))
    page = request.GET.get("page", 1)
    try:
        paginator = Paginator(equipos, 4)
        equipos = paginator.page(page)
    except:
        raise Http404

    if busqueda:
        equipos = Equipo.objects.filter(
            Q(num_serie__icontains=busqueda) |
            Q(marca__icontains=busqueda) |
            Q(modelo__icontains=busqueda) |
            Q(tipo_equipo__icontains=busqueda) |
            Q(fecha_adquisicion__icontains=busqueda) |
            Q(fecha_puesta_marcha__icontains=busqueda) |
            Q(proveedor__nombre__icontains=busqueda) |
            Q(planta__nombre__icontains=busqueda)

        ).distinct()
    data = {"lista_equipos": equipos,
            "paginator": paginator}
    return render(request, "equipo_list.html", data)

# datos de un Equipos


def show_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    context = {"equipo": equipo}
    return render(request, "equipo_descripcion.html", context)

# Crear Equipo


class EquipoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación
    def get(self, request, *args, **kwargs):
        formulario = EquipoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'equipo_create.html', context)

    # Llamada para procesar la creación del ticket
    def post(self, request, *args, **kwargs):
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            # Volvemos a la lista de ticket
            return redirect('equipos')

        return render(request, 'equipo_create.html', {'formulario': formulario})

    # Modificar Equipo


class EquipoUpdateView(UpdateView):
    model = Equipo
    template_name = "equipo_update.html"
    success_url = "/aplicacion/equipos/"
    fields = ['num_serie', 'marca', 'modelo', 'tipo_equipo', 'fecha_adquisicion',
              'fecha_puesta_marcha', 'proveedor', 'planta']


# Borrar equipo
class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = "delete.html"
    success_url = "/aplicacion/equipos/"


# Lista de empleados
def index_empleados(request):
    busqueda = request.GET.get("buscar")
    empleados = get_list_or_404(Empleado.objects.order_by("DNI"))
    page = request.GET.get("page", 1)
    try:
        paginator = Paginator(empleados, 4)
        empleados = paginator.page(page)
    except:
        raise Http404

    if busqueda:
        empleados = Empleado.objects.filter(
            Q(DNI__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(apellido1__icontains=busqueda) |
            Q(apellido2__icontains=busqueda) |
            Q(email__icontains=busqueda) |
            Q(telefono__icontains=busqueda)
        ).distinct()

    data = {"lista_empleados": empleados,
            "paginator": paginator}
    return render(request, "empleado_list.html", data)


# Datos de empleado
def show_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    context = {"empleado": empleado}
    return render(request, "empleado_descripcion.html", context)

# Crear empleado


class EmpleadoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación
    def get(self, request, *args, **kwargs):
        formulario = EmpleadoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'empleado_create.html', context)

    # Llamada para procesar la creación del empleado
    def post(self, request, *args, **kwargs):
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            # Volvemos a la lista de empleado
            return redirect('empleados')

        return render(request, 'empleado_create.html', {'formulario': formulario})


# Modificar Empleado
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado_update.html"
    success_url = "/aplicacion/empleados/"
    fields = ['DNI', 'nombre', 'apellido1', 'apellido2', 'email',
              'telefono']

# Borrar empleado


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "delete.html"
    success_url = "/aplicacion/empleados/"


# Lista de Proveedores
def index_proveedores(request):
    busqueda = request.GET.get("buscar")
    proveedores = get_list_or_404(Proveedor.objects.order_by("nombre"))
    page = request.GET.get("page", 1)
    try:
        paginator = Paginator(proveedores, 4)
        proveedores = paginator.page(page)
    except:
        raise Http404
    if busqueda:
        proveedores = Proveedor.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(telefono__icontains=busqueda)
        ).distinct()
    data = {"lista_proveedores": proveedores,
            "paginator": paginator}
    return render(request, "proveedores_list.html", data)


class ProveedorListView(View):
    def get(self, request):
        prlist = Proveedor.objects.all()
        return JsonResponse(list(prlist.values()), safe=False)


# Datos de Proveedores

class ProveedorDetailView(View):
    def get(self, request, pk):
        proveedor = Proveedor.objects.get(pk=pk)
        return JsonResponse(model_to_dict(proveedor))


def show_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    context = {"proveedor": proveedor}
    return render(request, "proveedor_descripcion.html", context)

# Crear empleado


class ProveedorCreateView(View):
    # Llamada para mostrar la página con el formulario de creación
    def get(self, request, *args, **kwargs):
        formulario = ProveedorForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'proveedor_create.html', context)

    # Llamada para procesar la creación del empleado
    def post(self, request, *args, **kwargs):
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Volvemos a la lista de empleado
            return redirect('proveedores')

        return render(request, 'proveedor_create', {'formulario': formulario})

# Modificar Proveedor


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = "proveedor_update.html"
    success_url = "/aplicacion/proveedores/"
    fields = ['nombre', 'telefono']


# Borrar Proveedor

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "delete.html"
    success_url = "/aplicacion/proveedores/"

# Muestra el listado de tickets de un empleado concreto


def tickets_de_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    ticket = empleado.ticket_set.all()
    context = {'empleado': empleado, 'lista_tickets': ticket}
    return render(request, 'ticket_list.html', context)

# Muestra el listado de tickets de un equipo concreto


def tickets_de_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    ticket = equipo.ticket_set.all()
    context = {'equipo': equipo, 'lista_tickets': ticket}
    return render(request, 'ticket_list.html', context)

# Muestra el listado de equipos de un proveedor concreto


def equipos_de_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    equipo = proveedor.equipo_set.all()
    context = {'proveedor': proveedor, 'lista_equipos': equipo}
    return render(request, 'equipo_list.html', context)
