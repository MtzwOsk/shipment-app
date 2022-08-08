from django.views.generic import TemplateView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer, ShipmentUpdateOrCreateSerializer


class HomePageView(TemplateView):
    template_name = 'index.html'


class ShipmentViewSetAPI(CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin,
                         GenericViewSet):
    queryset = Shipment.objects.all()
    permission_classes = [AllowAny]

    serializer_map = {
        'GET': ShipmentSerializer,
        'POST': ShipmentUpdateOrCreateSerializer,
        'PUT': ShipmentUpdateOrCreateSerializer,
    }

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)
