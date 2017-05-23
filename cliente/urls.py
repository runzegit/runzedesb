from django.conf.urls import url
from rest_framework import routers
from .views import ClienteViewSet, DuplicataViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'duplicata', DuplicataViewSet)

urlpatterns = router.urls