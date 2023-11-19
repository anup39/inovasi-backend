from rest_framework.response import Response
from rest_framework import viewsets
from .models import Facility, Refinery, Mill
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

        try:
            df = pd.read_excel(excel_file, sheet_name=sheet)
            df.fillna(0, inplace=True)
            if sheet == "Facilites":
                df['geom'] = df.apply(lambda row: Point(
                    row['facilities_long'], row['facilities_lat']), axis=1)
                facilities_data = df.to_dict(orient='records')

                # # Create Facility objects
                Facility.objects.bulk_create([Facility(
                    facilities_eq_id=data['facilities_eq_id'],
                    facilities_name=data['facilities_name'],
                    facilities_address=data['facilities_address'],
                    facilities_type=data['facilities_type'],
                    facilities_lat=data['facilities_lat'],
                    facilities_long=data['facilities_long'],
                    facilites_rspo=data['facilites_rspo'],
                    facilites_date_update=data['facilites_date_update'],
                    geom=data['geom'],
                    # Add other fields accordingly
                ) for data in facilities_data])

                return Response({'message': f'{sheet} Data uploaded successfully'}, status=status.HTTP_201_CREATED)
            if sheet == "Refinery":
                df['geom'] = df.apply(lambda row: Point(
                    row['refinery_long'], row['refinery_lat']), axis=1)
                refinery_data = df.to_dict(orient='records')

                # # Create Refinery objects
                Refinery.objects.bulk_create([Refinery(
                    refinery_eq_id=data['refinery_eq_id'],
                    refinery_name=data['refinery_name'],
                    refinery_address=data['refinery_address'],
                    refinery_type=data['refinery_type'],
                    refinery_lat=data['refinery_lat'],
                    refinery_long=data['refinery_long'],
                    refinery_rspo=data['refinery_rspo'],
                    refinery_date_update=data['refinery_date_update'],
                    geom=data['geom'],
                    # Add other fields accordingly
                ) for data in refinery_data])

                return Response({'message': f'{sheet} Data uploaded successfully'}, status=status.HTTP_201_CREATED)

            if sheet == "Mill":
                df['geom'] = df.apply(lambda row: Point(
                    row['mill_long'], row['mill_lat']), axis=1)
                mill_data = df.to_dict(orient='records')
                print(df.head().to_dict(orient='records'))

                Mill.objects.bulk_create([Mill(
                    mill_company_name=data['mill_company_name'],
                    mill_company_group_id=data['mill_company_group_id'],
                    mill_company_group=data['mill_company_group'],
                    mill_country=data['mill_country'],
                    mill_province=data['mill_province'],
                    mill_district=data['mill_district'],
                    mill_address=data['mill_address'],
                    mill_type=data['mill_type'],
                    mill_lat=data['mill_lat'],
                    mill_long=data['mill_long'],
                    mill_rspo=data['mill_rspo'],
                    mill_mspo=data['mill_mspo'],
                    mill_capacity=data['mill_capacity'],
                    mill_methane_capture=data['mill_methane_capture'],
                    mill_deforestation_risk=data['mill_deforestation_risk'],
                    mill_legal_prf_risk=data['mill_legal_prf_risk'],
                    mill_legal_production_forest=data['mill_legal_production_forest'],
                    mill_legal_conservation_area=data['mill_legal_conservation_area'],
                    mill_legal_landuse_risk=data['mill_legal_landuse_risk'],
                    mill_complex_supplybase_risk=data['mill_complex_supplybase_risk'],
                    mill_date_update=data['mill_date_update'],
                    geom=data['geom'],
                    # Add other fields accordingly
                ) for data in mill_data])

                return Response({'message': f'{sheet} Data uploaded successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': f'Error processing file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.filter(is_display=True)
    serializer_class = FacilitySerializer
