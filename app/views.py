from rest_framework.response import Response
from rest_framework import viewsets
from .models import Facility, Refinery, Mill
from .tasks import handleExampleTask
from .serializer import FileUploadSerializer, ShapeFileUploadSerializer, FacilitySerializer
from django.contrib.gis.geos import Point
from rest_framework import generics, status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import pandas as pd
import zipfile
import glob
from django.core.exceptions import ValidationError
import geopandas as gpd
from django.contrib.gis.geos import (
    GEOSGeometry)
# Create your views here.


def checkUploadFileValidationGlobal(shape_file):
    print("here validation")

    if not shape_file.name.endswith('.zip'):
        raise ValidationError('The file must be a ZIP archive.')
    if shape_file.name.endswith('.zip'):
        # Open the zip file
        with zipfile.ZipFile(shape_file, 'r') as zip_file:

            # Check if a file with a .shp extension exists in the zip file
            file_list = zip_file.namelist()
            shp_file = None
            for file_name in file_list:
                if file_name.endswith('.shp'):
                    shp_file = file_name
                    break

            # If a .shp file exists, open it
            if shp_file:
                with zip_file.open(shp_file) as file:
                    pass
            else:
                raise ValueError(
                    f"No .shp file found in {shape_file}")


def handleShapefileGlobal(shapefile_obj, model):
    shape_file = shapefile_obj
    with zipfile.ZipFile(shape_file, "r") as zip_ref:
        zip_ref.extractall(str(shape_file))
    shape = glob.glob(r'{}/**/*.shp'.format(str(shape_file)),
                      recursive=True)[0]
    gdf = gpd.read_file(shape)
    total_bounds = gdf.total_bounds
    bound_dict = {"total_bounds": total_bounds.tolist()}
    print(gdf.columns)
    for index, row in gdf.iterrows():
        # print(index, row)
        dropped_geometry = row.drop(["geometry"])
        dropped_geometry_dict = dropped_geometry.to_dict()
        geom = GEOSGeometry(str(row["geometry"]))

        print(geom.geom_type)

        # if geom.geom_type == "MultiPolygon":
        #     for polygon in geom:
        #         # new_geom = Polygon(polygon.exterior)
        #         model.objects.create(
        #             layer=layer, attributes=dropped_geometry_dict, geom=polygon)
        # else:
        #     model.objects.create(
        #         layer=layer,  attributes=dropped_geometry_dict, geom=geom)
        #     pass

    return bound_dict


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
        file = serializer.validated_data['file']

        try:
            if sheet == "Facilites":
                df = pd.read_excel(file, sheet_name=sheet)
                df.fillna(0, inplace=True)
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
                df = pd.read_excel(file, sheet_name=sheet)
                df.fillna(0, inplace=True)
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
                df = pd.read_excel(file, sheet_name=sheet)
                df.fillna(0, inplace=True)
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

            if sheet == "Shapefile":
                print(file, 'file')

                checkUploadFileValidationGlobal(file)

                handleShapefileGlobal(file, "Agriplot")

                return Response({'message': f'{sheet} Data uploaded successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': f'Error processing file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.filter(is_display=True)
    serializer_class = FacilitySerializer
