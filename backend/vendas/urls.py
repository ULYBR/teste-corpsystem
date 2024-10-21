from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendaViewSet, ItemVendaViewSet  # Verifique se esses imports estão corretos

router = DefaultRouter()
router.register(r'vendas', VendaViewSet)
router.register(r'itens-venda', ItemVendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
