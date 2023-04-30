from django import forms
from .models import Ticket,Equipo


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'