from django.test import TestCase
from django.urls import reverse
from .models import PrendasRopa
from .forms import PrendaForm, ComentarioForm


class PrendasTestCase(TestCase):
    def setUp(self):
        self.prenda = PrendasRopa.objects.create(
            Titulo='Camisa',
            Fecha='2024-01-01',  
            Precio=50.00,
        )

    def test_prenda_form_valid(self):
        form_data = {
            'Titulo': 'Nueva prenda',
            'Marca': 'Marca nueva',
            'Vendedor': 'Vendedor nuevo',
            'Descripcion': 'Descripción nueva',
            'Fecha': '2024-06-21',  
            'Precio': 100.00,
        }
        
        form_data['Fecha'] = str(form_data['Fecha'])
        form = PrendaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comentario_form_valid(self):
        form_data = {'comentario': 'Este es un comentario válido'}
        form = ComentarioForm(data=form_data)
        self.assertTrue(form.is_valid())
