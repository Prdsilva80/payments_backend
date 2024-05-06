from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # Endpoint adicional para processar pagamentos específicos
    @action(detail=True, methods=['post'])
    def process_payment(self, request, pk=None):
        payment = self.get_object()
        payment.status = 'Processed'
        payment.save()
        return Response({'status': 'payment processed'})
