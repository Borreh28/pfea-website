from django.urls import reverse_lazy
from django.views.generic import DetailView

from pfea_app.models import Voluntario

class SolicitudDeVoluntariosDetail(DetailView):
    template_name = 'models/voluntarios_solicitud_detalle.html'
    model = Voluntario