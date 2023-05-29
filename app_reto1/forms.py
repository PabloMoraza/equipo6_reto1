from django import forms
from .models import Empleado, Ticket, Equipo, Proveedor


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {
            "num_referencia": "Numero referencia",
            "fecha_apertura": "Fecha de apertura",
            "fecha_resolucion": "Fecha de resolucion",
            "tipo_ticket": "Tipo",
            "estado_ticket": "Estado",
            "empleado_asignado": "Empleado Asignado",
            "comentarios_ticket": "Comentarios"
        }
        widgets = {
            "equipo_a_reparar": forms.Select(attrs={'class': 'form-control'}),
            "num_referencia": forms.NumberInput(attrs={'class': 'form-control'}),
            "descripcion": forms.TextInput(attrs={'class': 'form-control'}),
            "detalles": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_apertura": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_resolucion": forms.TextInput(attrs={'class': 'form-control'}),
            "urgencia": forms.Select(attrs={'class': 'form-control'}),
            "tipo_ticket": forms.Select(attrs={'class': 'form-control'}),
            "estado_ticket": forms.Select(attrs={'class': 'form-control'}),
            "empleado_asignado": forms.Select(attrs={'class': 'form-control'}),
            "comentarios_ticket": forms.TextInput(attrs={'class': 'form-control'})
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        labels = {
            "num_serie": "Numero de Serie",
            "tipo_equipo": "Tipo de Equipo",
            "fecha_adquisicion": "Fecha de Adquisicion (MM/DD/AAAA)",
            "fecha_puesta_marcha": "Fecha de Puesta en Marcha (MM/DD/AAAA)"
        }
        widgets = {
            "num_serie": forms.NumberInput(attrs={'class': 'form-control'}),
            "marca": forms.TextInput(attrs={'class': 'form-control'}),
            "modelo": forms.TextInput(attrs={'class': 'form-control'}),
            "tipo_equipo": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_adquisicion": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_puesta_marcha": forms.TextInput(attrs={'class': 'form-control'}),
            "proveedor": forms.Select(attrs={'class': 'form-control'}),
            "planta": forms.Select(attrs={'class': 'form-control'})}


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        labels = {
            "apellido1": "Primer Apellido",
            "apellido2": "Segundo Apellido"
        }
        widgets = {
            "DNI": forms.TextInput(attrs={'class': 'form-control'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido1": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido2": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.TextInput(attrs={'class': 'form-control'}),
            "telefono": forms.NumberInput(attrs={'class': 'form-control'})}


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "telefono": forms.NumberInput(attrs={'class': 'form-control'})
        }
