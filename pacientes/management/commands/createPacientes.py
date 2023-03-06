import faker
from django.core.management.base import BaseCommand
from pacientes.models import *
from faker import Faker
import random

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--cantidad', type=int, default=0)
        parser.add_argument('--bd', type=str)

    def handle(self, *args, **kwargs):
        cantidad = kwargs.get('cantidad')
        bd = kwargs.get('bd')

        

