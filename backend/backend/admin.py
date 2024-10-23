from django.contrib import admin
from .models import Cliente, Produto, Vendedor, Venda, ItemVenda

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Vendedor)
admin.site.register(Venda)
admin.site.register(ItemVenda)
