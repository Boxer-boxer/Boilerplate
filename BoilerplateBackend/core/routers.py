from rest_framework import routers

from . import viewsets
from . import views

router = routers.DefaultRouter()
router.register('', viewsets.CustomUserModelViewSet)