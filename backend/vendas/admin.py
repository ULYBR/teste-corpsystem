from django.contrib import admin
from .models import Venda, ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_venda', 'valor_total')
    search_fields = ('cliente__nome',)
    inlines = [ItemVendaInline]

admin.site.register(Venda, VendaAdmin)
