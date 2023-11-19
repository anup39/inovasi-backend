from rest_framework.response import Response
from rest_framework import viewsets
from .models import Facility
from .tasks import handleExampleTask
from .serializer import FileUploadSerializer, FacilitySerializer
from django.contrib.gis.geos import Point
from rest_framework import generics, status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import pandas as pd
# Create your views here.


class ExampleViewSet(viewsets.ViewSet):
    def list(self, request):
        # Your logic for processing the API request
        data = {
            'message': 'Hello, API!',
            'status': 'success'
        }
        # handleExampleTask.delay()

        return Response(data)


class FileUploadAPIView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sheet = serializer.validated_data['sheet']
        excel_file = serializer.validated_data['file']

        print(excel_file, 'excel file')
        print(sheet, 'sheet')

        # Process Excel file using Pandas
        try:
            print(excel_file, 'file excel')
            df = pd.read_excel(excel_file, sheet_name="Facilites")
            print(df.head(), 'df head')
            df.fillna(0, inplace=True)
            df['geom'] = df.apply(lambda row: Point(
                row['facilities_long'], row['facilities_lat']), axis=1)
            facilities_data = df.to_dict(orient='records')

            # # # Create Facility objects
            # Facility.objects.bulk_create([Facility(
            #     facilities_eq_id=data['facilities_eq_id'],
            #     facilities_address=data['facilities_address'],
            #     facilities_type=data['facilities_type'],
            #     facilities_lat=data['facilities_lat'],
            #     facilities_long=data['facilities_long'],
            #     facilites_rspo=data['facilites_rspo'],
            #     facilites_date_update=data['facilites_date_update'],
            #     geom=data['geom'],
            #     # Add other fields accordingly
            # ) for data in facilities_data])

            return Response({'message': 'Data uploaded successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': f'Error processing file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.filter(is_display=True)
    serializer_class = FacilitySerializer
