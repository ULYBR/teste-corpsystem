from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendedorViewSet

router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
