from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shipments.models import Shipment


class ShipmentDataMixin:

    @classmethod
    def setUpTestData(cls):
        cls.shipment = Shipment.objects.create(title='Title', pickup_address='Warsaw', delivery_address='NY')


class CreateViewAPITest(APITestCase):

    def test_create_shipment(self):
        url = reverse('shipment_api:shipment-list')
        title: str = 'Test Title'
        payload: dict = {
            'title': title,
            'pickup_address': 'Warsaw',
            'delivery_address': 'NY'
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Shipment.objects.filter(title=title).exists())


class RetrieveShipmentViewAPITest(ShipmentDataMixin, APITestCase):

    def test_retrieve_shipment(self):
        url = reverse('shipment_api:shipment-detail', args=[self.shipment.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.data.get('id'), self.shipment.id)


class ListShipmentApiViewTest(ShipmentDataMixin, APITestCase):

    def setUp(self):
        self.shipment_2 = Shipment.objects.create(title='Title', pickup_address='Prague', delivery_address='Milano')

    def test_list_shipment(self):
        """
        Listing shipments
        """
        url = reverse('shipment_api:shipment-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0].get('id'), self.shipment.id)
        self.assertEqual(response.data[1].get('id'), self.shipment_2.id)


class DeleteShipmentApiViewTest(ShipmentDataMixin, APITestCase):

    def test_delete_shipment(self):
        url = reverse('shipment_api:shipment-detail', args=[self.shipment.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Shipment.objects.count(), 0)


class UpdateShipmentAPIViewTest(ShipmentDataMixin, APITestCase):

    def test_update_shipment(self):
        url = reverse('shipment_api:shipment-detail', args=[self.shipment.pk])
        new_title: str = 'New Title'
        changed_data_payload: dict = {
            'title': new_title,
            'pickup_address': 'Yutz',
            'delivery_address': 'Metz',
        }
        response = self.client.put(url, data=changed_data_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shipment.objects.get(id=self.shipment.id).title, new_title)
