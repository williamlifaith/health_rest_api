from django.urls import path
from django.conf.urls import url,include
from .views import PatientViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register('query', PatientViewSet, basename='patient')


urlpatterns = [
    url('', include(router.urls)),
]