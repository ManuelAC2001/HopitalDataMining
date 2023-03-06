from django.db import models

# Create your models here.
class Medicamento(models.Model):
    laboratorio = models.CharField(max_length=50, null=False)
    nombre_generico = models.CharField(max_length=30, null=False)
    via_administracion = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre_generico
    
    class Meta:
        db_table = "medicamentos"
        

class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=30, null=False)
    ape_pa_paciente = models.CharField(max_length=30, null=False)
    ape_ma_paciente = models.CharField(max_length=30, null=False)

    edad_paciente = models.SmallIntegerField(null=False)

    peso_paciente = models.FloatField(null=False)
    estatura_paciente = models.FloatField(null=False)
    fecha_naci_paciente = models.DateField()
    sexo_paciente = models.CharField(max_length=2)
    telefono_paciente = models.CharField(max_length=15)
    direccion_paciente = models.CharField(max_length=150)
    padecimientos_paciente = models.CharField(max_length=50)
    alergias_paciente = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_paciente
    

    class Meta:
        db_table = "pacientes"

class Receta(models.Model):
    fecha_receta = models.DateField(null=False)
    hora_receta = models.TimeField(null=False)
    dosis_medicamento = models.CharField(max_length=70, null=False)

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamentos = models.ManyToManyField(Medicamento)

    class Meta:
        db_table = "recetas"