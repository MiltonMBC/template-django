from django.db import models

# Create your models here.

class Administrador(models.Model):
    idAdministrador = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombreEmpresa = models.CharField(max_length=30)
    rutEmpresa = models.IntegerField()
    rut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    celular_Telefono = models.IntegerField()
    password = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

class Cotizacion(models.Model):
    idProyecto = models.IntegerField()
    idCotizacion = models.IntegerField()
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombreProyecto_Cantidad = models.CharField(max_length=30)
    costo_Total = models.IntegerField()
    descripcion = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30)

    class Meta:
        unique_together = ('idProyecto', 'idCotizacion')


class GerenteAdmin(models.Model):
    idGerenteAdmin = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)    

class Empleados(models.Model):
    idEmpleados = models.AutoField(primary_key=True)
    idAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    idGerenteAdmin = models.ForeignKey(GerenteAdmin, on_delete=models.CASCADE)
    rol = models.CharField(max_length=30)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    celular = models.IntegerField()
    correo = models.CharField(max_length=30)
    capacitacion = models.CharField(max_length=30)


class GestionNomina(models.Model):
    idGestionNomina = models.AutoField(primary_key=True)
    idEmpleados = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    sueldo = models.IntegerField()
    horasTrabajadas = models.IntegerField()
    descansos = models.CharField(max_length=30)
    tipoPago = models.IntegerField()

class HistorialLaboral(models.Model):
    idHistoriaLab = models.AutoField(primary_key=True)
    idEmpleados = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    permisos = models.CharField(max_length=30)
    licenciasMedicas = models.CharField(max_length=30)
    fallas = models.CharField(max_length=30)
    comportamiento = models.CharField(max_length=30)
    despido_Renuncia = models.BooleanField()

class Inventario(models.Model):
    idEmpleados = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    idArticulo = models.IntegerField()
    nombreArticulo = models.CharField(max_length=30)
    estadoArticulo = models.CharField(max_length=30)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('idEmpleados', 'idArticulo')


class Proyecto(models.Model):
    idProyecto = models.AutoField(primary_key=True)
    nombreProyecto = models.CharField(max_length=30)
    costo = models.IntegerField()
