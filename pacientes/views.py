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
        

