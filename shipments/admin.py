from django.contrib import admin

# Register your models here.
from shipments.models import ShipmentModel

admin.site.register(ShipmentModel)
