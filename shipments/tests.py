from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from shipments.models import ShipmentModel


class TestShipmentViewSet(APITestCase):

    def test_create_shipment(self):
        """
        Create Shipment
        """
        url = reverse('shipment_api:shipment-list')
        title: str = 'Test Title'
        data = {'title': title}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
        self.assertEqual(ShipmentModel.objects.filter(title=title).exists(), True)

    def test_delete_shipment(self):
        """
        Delete shipment through api
        """
        shipment = ShipmentModel.objects.create(title='Title')
        url = reverse('shipment_api:shipment-detail', args=[shipment.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ShipmentModel.objects.count(), 0)

    def test_update_shipment(self):
        """
        Update shipment
        """
        shipment = ShipmentModel.objects.create(title='Old Title')
        url = reverse('shipment_api:shipment-detail', args=[shipment.pk])

        new_title: str = 'New Title'
        changed_data: dict = {
            'title': new_title
        }
        response = self.client.put(url, data=changed_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ShipmentModel.objects.get(id=shipment.id).title, new_title)

    def test_list_shipment(self):
        """
        Listing shipments
        """
        shipment_1 = ShipmentModel.objects.create(title='Old Title')
        shipment_2 = ShipmentModel.objects.create(title='Old Title')
        url = reverse('shipment_api:shipment-list')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0].get('id'), shipment_1.id)
        self.assertEqual(response.data[1].get('id'), shipment_2.id)

    def test_retrieve_shipment(self):
        """
        Get shipments
        """
        shipment = ShipmentModel.objects.create(title='Old Title')
        url = reverse('shipment_api:shipment-detail', args=[shipment.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.data.get('id'), shipment.id)
