from django.db import models

# Create your models here.

class Hospital(models.Model):
    rfc_hospital = models.CharField(max_length=10, primary_key=True, null=False)
    cp_hospital = models.CharField(max_length=12, null=False)
    nombre_hospital = models.CharField(max_length=30, null=False)
    telefono_hospital = models.CharField(max_length=15, null=False)
    direccion_hospital = models.CharField(max_length=250, null=False)

class Medicamentos(models.Model):
    id_medicamento = models.CharField(max_length=10, primary_key=True, null=False)
    laboratorio = models.CharField(max_length=30, null=False)
    nombre_generico = models.CharField(max_length=30, null=False)
    nombre_comercial = models.CharField(max_length=30, null=False)
    via_administracion = models.CharField(max_length=30, null=False)
    forma_farmaceutica = models.CharField(max_length=30, null=False)
    concentracion = models.CharField(max_length=30, null=False)

class Paciente(models.Model):
    id_paciente = models.CharField(max_length=10, primary_key=True, null=False)
    nombre_paciente = models.CharField(max_length=30, null=False)
    ape_pa_paciente = models.CharField(max_length=30, null=False)
    ape_ma_paciente = models.CharField(max_length=30, null=False)
    edad_paciente = models.IntegerField(max_length=2, null=False)
    peso_paciente = models.FloatField(null=False)
    estatura_paciente = models.FloatField(null=False)
    fecha_naci_paciente = models.DateField()
    sexo_paciente = models.CharField(max_length=2)
    telefono_paciente = models.CharField(max_length=15)
    direccion_paciente = models.CharField(max_length=50)
    padecimientos_paciente = models.CharField(max_length=50)
    alergias_paciente = models.CharField(max_length=50)

class Pago(models.Model):
    id_transaccion = models.IntegerField(primary_key=True)
    descripcion_pago = models.CharField(max_length=100, null=False)
    monto_pago_caja = models.FloatField(null=False)
    fecha_pago_caja = models.FloatField(null=False)
    hora_pago_caja = models.TimeField(null=False)
    rfc_hospital = models.CharField(max_length=10)
    rfc_hospital = models.CharField(max_length=10) # esta y la de abajo llevan FK no le entendi bien al pedo 
    id_paciente = models.CharField(max_length=10)

class RecetaMedica(models.Model):
    id_receta = models.CharField(max_length=10, primary_key=True, null=False)
    fecha_receta = models.DateField(null=False)
    hora_receta = models.TimeField(null=False)
    dosis_medicamento = models.CharField(max_length=70, null=False)
    id_medicamento = models.CharField(max_length=10)
    id_consulta = models.CharField(max_length=10)