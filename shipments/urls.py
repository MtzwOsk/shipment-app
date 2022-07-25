from sys import path

from rest_framework import routers
from shipments.views import ShipmentViewSetAPI

app_name = 'shipments'

router = routers.SimpleRouter()
router.register(r'shipments', ShipmentViewSetAPI, basename='shipment')

urlpatterns = router.urls
