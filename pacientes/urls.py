from django.urls import  path
from . import  views 

app_name = 'pacientes'

urlpatterns = [
    path('', views.HospitalView.as_view(), name="pacientes"),
    path('medicamentos', views.MedicamentosView.as_view(), name="pacientes"),
]
