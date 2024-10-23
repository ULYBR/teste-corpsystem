

from django.test import TestCase
from .models import Cliente  # Altere isso para o modelo que deseja testar

class ClienteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(nome='Teste Cliente', email='teste@cliente.com')

    def test_cliente_email(self):
        cliente = Cliente.objects.get(id=1)
        self.assertEqual(cliente.email, 'teste@cliente.com')
