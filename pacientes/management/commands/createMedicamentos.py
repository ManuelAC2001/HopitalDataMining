import faker
from django.core.management.base import BaseCommand
from pacientes.models import *
from faker import Faker

MEDICAMENTOS_NOMBRES = [
    "Simvastatina",
    "Aspirina",   
    "Omeprazol",   
    "Ramipril",   
    "Amlodipina",   
    "Paracetamol",   
    "Atorvastatina",   
    "Salbutamol",   
    "Lansoprazol",   
]

VIAS_ADMINISTRACION_NOMBRES = [
    "Rectal",
    "Vaginal",
    "Ótica",
    "Nasal",
    "Cutánea",
    "Transdérmica", 
]

class Provider(faker.providers.BaseProvider):
    def nombre_medicamento(self): 
        return self.random_element(MEDICAMENTOS_NOMBRES)
    
    def via_administracion(self):
        return self.random_element(VIAS_ADMINISTRACION_NOMBRES)

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
            laboratorio = fake.company()
            nombre_generico = fake.nombre_medicamento()
            via_administracion = fake.via_administracion()

            medicamento = Medicamento(
                laboratorio = laboratorio,
                nombre_generico = nombre_generico,
                via_administracion = via_administracion
            )

            medicamento.save(using=bd)

            self.stdout.write(self.style.SUCCESS('%s.-Medicamento agregado correctamente' % (i+1)))



