from rest_framework import routers
from .views import ExampleViewSet, FileUploadAPIView, FacilityViewSet, PieChartViewSet
from django.urls import path, include


router = routers.DefaultRouter()

router.register('facility', FacilityViewSet, basename='facility')

urlpatterns = [
    path('', include(router.urls)),
    path('app/example', ExampleViewSet.as_view({'get': 'list'}),
         name='example-api'),
    path('upload-facility/', FileUploadAPIView.as_view(),
         name='upload-facility'),
    path('pie-chart/<section>/<distinct>/', PieChartViewSet.as_view(),
         name='pie-chart'),
]
