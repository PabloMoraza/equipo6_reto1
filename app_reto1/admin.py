from django.contrib import admin
from .models import Empleado , Proveedor , Planta, Equipo, Urgencia, Tipo_ticket, Estado_ticket, Ticket

admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Planta)
admin.site.register(Equipo)
admin.site.register(Urgencia)
admin.site.register(Tipo_ticket)
admin.site.register(Estado_ticket)
admin.site.register(Ticket)
