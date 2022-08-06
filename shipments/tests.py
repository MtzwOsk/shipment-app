from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shipments.models import Shipment


class TestShipmentViewSet(APITestCase):

    def test_create_shipment(self):
        """
        Create Shipment
        """
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

    def test_delete_shipment(self):
        """
        Delete shipment through api
        """
        shipment = Shipment.objects.create(title='Title', pickup_address='Warsaw', delivery_address='NY')
        url = reverse('shipment_api:shipment-detail', args=[shipment.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shipment.objects.count(), 0)

    def test_update_shipment(self):
        """
        Update shipment
        """
        shipment = Shipment.objects.create(title='Old Title', pickup_address='Warsaw', delivery_address='NY')
        url = reverse('shipment_api:shipment-detail', args=[shipment.pk])

        new_title: str = 'New Title'
        changed_data_payload: dict = {
            'title': new_title,
            'pickup_address': 'Yutz',
            'delivery_address': 'Metz'
        }
        response = self.client.put(url, data=changed_data_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shipment.objects.get(id=shipment.id).title, new_title)

    def test_list_shipment(self):
        """
        Listing shipments
        """
        shipment_1 = Shipment.objects.create(title='For friend', pickup_address='Warsaw', delivery_address='NY')
        shipment_2 = Shipment.objects.create(title='Glass', pickup_address='Warsaw', delivery_address='NY')
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
        shipment = Shipment.objects.create(title='Fridge', pickup_address='Warsaw', delivery_address='NY')
        url = reverse('shipment_api:shipment-detail', args=[shipment.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.data.get('id'), shipment.id)
