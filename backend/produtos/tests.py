from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Produto

class ProdutoViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.produto = Produto.objects.create(
            nome='Teste Produto',
            descricao='Descrição do produto',
            preco=19.99,
            estoque=100
        )
        cls.client = APIClient()

    def test_get_produto(self):
      """Testa a recuperação de um produto existente."""
      url = reverse('produto-detail', args=[self.produto.id])
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data['nome'], 'Teste Produto')


    def test_create_produto(self):
        """Testa a criação de um novo produto."""
        url = reverse('produto-list')
        data = {
            'nome': 'Novo Produto',
            'descricao': 'Nova descrição',
            'preco': 29.99,
            'estoque': 50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(Produto.objects.count(), 2)
        self.assertEqual(Produto.objects.get(id=response.data['id']).nome, 'Novo Produto')

    def test_update_produto(self):
      """Testa a atualização de um produto existente."""
      url = reverse('produto-detail', args=[self.produto.id])
      data = {
          'nome': 'Produto Atualizado',
          'descricao': 'Descrição atualizada',
          'preco': 39.99,
          'estoque': 200
      }
      response = self.client.put(url, data, format='json', content_type='application/json')
      self.produto.refresh_from_db()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(self.produto.nome, 'Produto Atualizado')


    def test_delete_produto(self):
      """Testa a exclusão de um produto existente."""
      url = reverse('produto-detail', args=[self.produto.id])
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertEqual(Produto.objects.count(), 0)

