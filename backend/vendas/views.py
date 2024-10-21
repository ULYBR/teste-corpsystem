from rest_framework import viewsets
from .models import Venda, ItemVenda  # Supondo que você tenha um modelo para Venda e ItemVenda
from .serializers import VendaSerializer, ItemVendaSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
