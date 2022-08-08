from django.contrib import admin

# Register your models here.
from shipments.models import Shipment

admin.site.register(Shipment)
