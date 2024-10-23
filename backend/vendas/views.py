from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Venda
from .serializers import VendaSerializer
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    # Retornar vendas em JSON (ação adicional)
    @action(detail=False, methods=['get'])
    def listar_vendas(self, request):
        vendas = self._filtrar_vendas(request)
        serializer = VendaSerializer(vendas, many=True)
        return Response(serializer.data)

    # Relatório em Excel
    @action(detail=False, methods=['get'])
    def relatorio(self, request):
        vendas = self._filtrar_vendas(request)

        # Exportar para Excel
        df = pd.DataFrame(list(vendas.values()))
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Vendas')
        writer.save()
        output.seek(0)

        response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.xlsx"'
        return response

    # Relatório em PDF
    @action(detail=False, methods=['get'])
    def relatorio_pdf(self, request):
        vendas = self._filtrar_vendas(request)

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Cabeçalho
        p.drawString(100, height - 50, "Relatório de Vendas")

        # Adicionar as vendas
        y_position = height - 80
        for venda in vendas:
            p.drawString(100, y_position, f"Venda ID: {venda.id}, Cliente: {venda.cliente}, Vendedor: {venda.vendedor}")
            y_position -= 20
            if y_position < 50:
                p.showPage()
                y_position = height - 50

        p.save()
        buffer.seek(0)

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.pdf"'
        return response

    # Método auxiliar para filtrar vendas
    def _filtrar_vendas(self, request):
        vendedor_id = request.GET.get('vendedor_id')
        cliente_id = request.GET.get('cliente_id')
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')

        vendas = Venda.objects.all()

        if vendedor_id:
            vendas = vendas.filter(vendedor_id=vendedor_id)
        if cliente_id:
            vendas = vendas.filter(cliente_id=cliente_id)
        if data_inicio and data_fim:
            vendas = vendas.filter(data__range=[data_inicio, data_fim])

        return vendas
