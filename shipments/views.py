from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ViewSet, ModelViewSet

from shipments.models import ShipmentModel
from shipments.serializers import ShipmentSerializer, ShipmentCreateSerializer


class ShipmentViewSetAPI(ModelViewSet):
    queryset = ShipmentModel.objects.filter()
    permission_classes = [AllowAny]  # MVP

    def list(self, request):
        queryset = ShipmentModel.objects.all()
        serializer = ShipmentSerializer(queryset, many=True)  # TODO status not remove
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ShipmentModel.objects.all()
        shipment = get_object_or_404(queryset, pk=pk)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = ShipmentModel.objects.all()
        shipment = get_object_or_404(queryset, pk=pk)
        # shipment.status = 'Canceled' # TODO
        shipment.delete()
        return Response(status=200)

    def update(self, request, pk=None):
        queryset = ShipmentModel.objects.all()
        shipment = get_object_or_404(queryset, pk=pk)
        serializer = ShipmentSerializer(shipment, data=self.request.data)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        return Response(serializer.data)

    def create(self, request):
        serializer = ShipmentCreateSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

