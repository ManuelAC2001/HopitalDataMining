from django.views.generic.base import TemplateView

from pacientes.models import *

class HospitalView(TemplateView):
    
    template_name = "pacientes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pacientes_mysql"] = Paciente.objects.using('mysql') 
        context["pacientes_pg"] = Paciente.objects.using('postgres') 
        context["pacientes_mdb"] = Paciente.objects.using('mariadb')
        return context
    
class MedicamentosView(TemplateView):
    template_name = "medicamentos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medicamentos_mysql"] = Medicamento.objects.using('mysql') 
        context["medicamentos_pg"] = Medicamento.objects.using('postgres') 
        context["medicamentos_mdb"] = Medicamento.objects.using('mariadb') 
        return context
    
        

