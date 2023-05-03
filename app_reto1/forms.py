from django import forms
from .models import Empleado, Ticket, Equipo, Proveedor


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
