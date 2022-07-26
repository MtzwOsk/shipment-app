from rest_framework.serializers import ModelSerializer

from shipments.models import Shipment


class ShipmentSerializer(ModelSerializer):

    class Meta:
        model = Shipment
        fields = ['title', 'id', 'status', 'created_at', 'description', 'pickup_address', 'delivery_address']
        read_only_fields = ['status', 'created_at']
