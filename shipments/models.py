import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ShipmentStatus(models.TextChoices):
    ORDERED = _('Ordered')
    PACKED = _('Packed')
    IN_TRANSIT = _('In Transit')
    DELIVERED = _('Delivered')


class ShippingAddressModel(models.Model):
    name = models.CharField('Full name', max_length=1024)
    address1 = models.CharField('Address line 1', max_length=1024)
    address2 = models.CharField('Address line 2', max_length=1024)
    zip_code = models.CharField('ZIP / Postal code', max_length=12)
    city = models.CharField('City', max_length=255)
    country = models.CharField('Country', max_length=3)  # TODO  choices=ISO_3166_CODES)
    address_email = models.EmailField('E-mail')

    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'


class ShipmentModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=127, choices=ShipmentStatus.choices, default=ShipmentStatus.ORDERED)

    # address = models.ForeignKey('shipments.ShippingAddressModel', on_delete=SET_NULL)
    # sender = models.ForeignKey(User, on_delete=SET_NULL) # TODO

    class Meta:
        verbose_name = 'Shipment'
        verbose_name_plural = 'Shipments'

    def __str__(self):
        return f'{self.title}'
