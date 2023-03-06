import faker
from django.core.management.base import BaseCommand
from pacientes.models import *
from faker import Faker
import random

DOSIS = [
    "900 mg/d",
    "900mg/3",
    "c/8h",
    "1125mg/día",
]

def get_pacientes_pk(bd):
    return Paciente.objects.using(bd).values_list('pk', flat=True)

def get_medicamentos_pk(bd):
    return Medicamento.objects.using(bd).values_list('pk', flat=True)

class Provider(faker.providers.BaseProvider):
    def paciente(self, bd):
        PACIENTES_PK = get_pacientes_pk(bd)
        return self.random_element(PACIENTES_PK)
    
    def medicamento(self, bd):
        MEDICAMENTOS_PK = get_medicamentos_pk(bd)
        return self.random_element(MEDICAMENTOS_PK)
    
    def dosis(self):
        return self.random_element(DOSIS)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--cantidad', type=int, default=0)
        parser.add_argument('--bd', type=str)
    
    def handle(self, *args, **kwargs):
        fake = Faker(['es_MX'])
        fake.add_provider(Provider)

        cantidad = kwargs.get('cantidad')
        bd = kwargs.get('bd')

        for i in range(cantidad):

            fecha_receta = fake.date_this_year(before_today=False, after_today=False)
            hora_receta = fake.time()
            dosis_medicamento = fake.dosis()
            paciente_id = fake.paciente(bd)

            receta = Receta(
                fecha_receta = fecha_receta,
                hora_receta = hora_receta,
                dosis_medicamento = dosis_medicamento,
                paciente_id = paciente_id
            )

            receta.save(using=bd)
            
            fake_medicamento = Faker()
            fake_medicamento.add_provider(Provider)
            medicamentos_cantidad = len(get_medicamentos_pk(bd))

            for _ in range( random.randint( 1, medicamentos_cantidad )):
                medicamento_id = fake_medicamento.unique.medicamento(bd)
                medicamento = Medicamento.objects.using(bd).get(pk=medicamento_id)
                receta.medicamentos.add(medicamento)