from typing import List

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ViewSet

from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer, ShipmentCreateSerializer


class HomePageView(TemplateView):
    template_name = 'index.html'


class ShipmentViewSetAPI(ViewSet):
    queryset = Shipment.objects.filter()
    permission_classes = [AllowAny]
    authentication_classes: List = []

    def list(self, request):
        queryset = Shipment.objects.all()
        serializer = ShipmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Shipment.objects.all()
        shipment = get_object_or_404(queryset, pk=pk)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Shipment.objects.all()
        shipment = get_object_or_404(queryset, pk=pk)
        shipment.delete()
        return Response(status=200)

    def update(self, request, pk=None):
        queryset = Shipment.objects.all()
        shipment = get_object_or_404(queryset, pk=pk)
        serializer = ShipmentCreateSerializer(shipment, data=self.request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def create(self, request):
        serializer = ShipmentCreateSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status=HTTP_201_CREATED)
