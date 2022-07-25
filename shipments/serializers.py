from rest_framework.serializers import ModelSerializer

from shipments.models import ShipmentModel


class ShipmentSerializer(ModelSerializer):
    class Meta:
        model = ShipmentModel
        fields = ['title', 'id', 'status', 'created_at']


class ShipmentCreateSerializer(ModelSerializer):

    class Meta:
        model = ShipmentModel
        fields = ['title', 'description']
