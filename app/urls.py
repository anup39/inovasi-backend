from rest_framework import routers
from .views import ExampleViewSet, FacilityFileUploadAPIView, FacilityViewSet
from django.urls import path, include


router = routers.DefaultRouter()

router.register('facility', FacilityViewSet, basename='facility')

urlpatterns = [
    path('', include(router.urls)),
    path('app/example', ExampleViewSet.as_view({'get': 'list'}),
         name='example-api'),
    path('upload-facility/', FacilityFileUploadAPIView.as_view(),
         name='upload-facility'),
]
