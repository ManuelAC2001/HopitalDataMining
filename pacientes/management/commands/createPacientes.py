import faker
from django.core.management.base import BaseCommand
from pacientes.models import *
from faker import Faker
import random

PADECIMIENTOS_NOMBRES = [
    "Bronquitis aguda",
    "Resfriado común",
    "Infección de oído",
    "Infecciones de la piel",
    "Dolor de garganta",
    "Infección urinaria",
]

ALERGIAS_NOMBRES = [
    "Alergia a alimentos",
    "Alergia a fármacos",
    "Asma alérgico",
    "Dermatitis atópica",
    "Poliposis nasal",
    "Rinitis alérgica",
    "Urticaria crónica"
]

class Provider(faker.providers.BaseProvider):
    def padecimiento(self):
        return self.random_element(PADECIMIENTOS_NOMBRES)

    def alergia(self):
        return self.random_element(ALERGIAS_NOMBRES)

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
            nombre_paciente = fake.first_name()
            ape_pa_paciente = fake.last_name() 
            ape_ma_paciente = fake.last_name() 
            edad_paciente = random.randint(0, 99)
            peso_paciente = round(random.uniform(10, 200), 2)  
            estatura_paciente = round(random.uniform(1, 2.05), 2)  
            fecha_naci_paciente = fake.date_of_birth(minimum_age= edad_paciente,maximum_age=edad_paciente)
            sexo_paciente = random.choice(['M', 'H'])
            telefono_paciente = fake.msisdn()
            direccion_paciente = fake.street_address()
            padecimientos_paciente = fake.padecimiento()
            alergias_paciente = fake.alergia()

            paciente = Paciente(
                nombre_paciente=nombre_paciente,
                ape_pa_paciente = ape_pa_paciente,
                ape_ma_paciente = ape_ma_paciente,
                edad_paciente = edad_paciente,
                peso_paciente =peso_paciente,
                estatura_paciente = estatura_paciente,
                fecha_naci_paciente = fecha_naci_paciente,
                sexo_paciente = sexo_paciente,
                telefono_paciente = telefono_paciente,
                direccion_paciente = direccion_paciente,
                padecimientos_paciente = padecimientos_paciente,
                alergias_paciente = alergias_paciente
            )

            paciente.save(using=bd)

            self.stdout.write(self.style.SUCCESS('%s.-Paciente agregado correctamente' % (i+1)))

