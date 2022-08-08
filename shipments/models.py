from django.db import models
from django.utils.translation import gettext_lazy as _


class ShipmentStatus(models.TextChoices):
    ORDERED = _('Ordered')
    PACKED = _('Packed')
    IN_TRANSIT = _('In Transit')
    DELIVERED = _('Delivered')


class Shipment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=127, choices=ShipmentStatus.choices, default=ShipmentStatus.ORDERED)
    description = models.CharField(max_length=255, blank=True, null=False)
    pickup_address = models.CharField(max_length=512)
    delivery_address = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Shipment'
        verbose_name_plural = 'Shipments'

    def __str__(self):
        return f'{self.title}'
