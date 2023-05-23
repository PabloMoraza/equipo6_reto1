from django.db import models

# CLASE EMPLEADO CON SUS CARACTERISTICAS


class Empleado(models.Model):
    DNI = models.CharField(max_length=9)
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    telefono = models.IntegerField()

    # FUNCIÓN PARA QUE DEVUELVA EL NOMBRE, APELLIDO Y DNI DEL EMPLEADO
    def __str__(self):
        return self.DNI
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


# CLASE PROVEEDOR CON SUS CARACTERISTICAS
class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()

    # FUNCIÓN PARA QUE DEVUELVA EL NOMBRE Y TELEFONO DEL PROVEEDOR
    def __str__(self):
        return self.nombre


# CLASE PLANTA CON SUS CARACTERISTICAS
class Planta(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)

    # FUNCIÓN PARA QUE DEVUELVA EL NOMBRE DE LA PLANTA
    def __str__(self):
        return self.nombre


# CLASE EQUIPO CON SUS CARACTERISTICAS
class Equipo(models.Model):
    num_serie = models.IntegerField()
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    tipo_equipo = models.CharField(max_length=20)
    fecha_adquisicion = models.DateField()
    fecha_puesta_marcha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

    # FUNCIÓN PARA QUE DEVUELVA EL NUMERO DE SERIE, MODELO Y TIPO DEL EQUIPO SOLICITADO
    def __str__(self):
        return self.modelo
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


# CLASE URGENCIA CON SUS CARACTERISTICAS
class Urgencia(models.Model):
    gravedad = models.CharField(max_length=20)

    # FUNCIÓN PARA QUE DEVUELVA LA GRAVEDAD DE LA URGENCIA
    def __str__(self):
        return self.gravedad


# CLASE TIPO TICKET CON SUS CARACTERISTICAS
class Tipo_ticket(models.Model):
    tipo = models.CharField(max_length=20)

    # FUNCIÓN PARA QUE DEVUELVA EL TIPO DE TICKET
    def __str__(self):
        return self.tipo


# CLASE ESTADO TICKET CON SUS CARACTERISTICAS
class Estado_ticket(models.Model):
    estado = models.CharField(max_length=20)

    # FUNCIÓN PARA QUE DEVUELVA EL TIPO DE TICKET
    def __str__(self):
        return self.estado


# CLASE TICKET Y CARACTERISTICAS
class Ticket(models.Model):
    equipo_a_reparar = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    num_referencia = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    detalles = models.CharField(max_length=500)
    fecha_apertura = models.DateTimeField()
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    urgencia = models.ForeignKey(Urgencia, on_delete=models.CASCADE)
    tipo_ticket = models.ForeignKey(Tipo_ticket, on_delete=models.CASCADE)
    estado_ticket = models.ForeignKey(Estado_ticket, on_delete=models.CASCADE)
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    comentarios_ticket = models.CharField(
        max_length=500, null=True, blank=True)

    # FUNCIÓN PARA QUE DEVUELVA EL NUMERO DE REFERENCIA, DESCRIPCION Y EMPLEADO QUE SE ENCARGA DEL TICKET
    def __str__(self):
        return self.num_referencia
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
