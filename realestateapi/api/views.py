from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer,realestate_serializer,realestate_serializer_2
from .models import realestate_data,realestate_data_2
from django_filters.rest_framework import DjangoFilterBackend
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.response import Response


fs = FileSystemStorage(location="tmp/")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class realestate_data_view_set(viewsets.ModelViewSet):
    queryset = realestate_data_2.objects.all()
    serializer_class = realestate_serializer_2
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['total_floor']
    
    @action(detail=False,methods=["POST"])
    def upload_data(self, request):
        file = request.FILES['file']
        content = file.read()
        
        file_content = ContentFile(content)
        file_name = fs.save(
            "tmp.csv",file_content
        )
        
        tmp_file = fs.path(file_name)
        
        csv_file = open(tmp_file,errors="ignore",encoding="utf-8")
        reader = csv.reader(csv_file)
        next(reader)
        next(reader)
        
        data_list = []
        
        for i in reader:
            the_district = i[0]
            total_floor = i[10]
            building_state = i[11]
            
            data_list.append(
                realestate_data_2(
                    the_district=the_district,
                    total_floor=total_floor,
                    building_state=building_state
                )
            )
        realestate_data_2.objects.bulk_create(data_list)
        
        '''for id_,row in enumerate(reader):
            (
                the_district,
                transaction_sign,
                number_plate,
                area_square_meter,
                use_zoning,
                non_metropolis,
                non_metropolis_use,
                transaction_date,
                transaction_pen_number,
                shifting_level,
                total_floor,
                building_state,
                main_use,
                main_building_material,
                construction_complete_year,
                building_shifting_total_area,
                building_present_situation_pattern_room,
                building_present_situation_pattern_hall,
                building_present_situation_pattern_health,
                building_present_situation_pattern_compartmented,
                has_manages_organization,
                total_price,
                the_unit_price,
                the_berth_category,
                berth_shifting_total_area_square_meter,
                the_berth_total_price,
                note,
                serial_number,
                main_building_area,
                ancillary_building_area,
                balcony_area,
                elevator,
                transfer_numder
            ) = row
            
            data_list.append(
                realestate_data(the_district=the_district,
                transaction_sign=transaction_sign,
                number_plate=number_plate,
                area_square_meter=area_square_meter,
                use_zoning=use_zoning,
                non_metropolis=non_metropolis,
                non_metropolis_use=non_metropolis_use,
                transaction_date=transaction_date,
                transaction_pen_number=transaction_pen_number,
                shifting_level=shifting_level,
                total_floor=total_floor,
                building_state=building_state,
                main_use=main_use,
                main_building_material=main_building_material,
                construction_complete_year=construction_complete_year,
                building_shifting_total_area=building_shifting_total_area,
                building_present_situation_pattern_room=building_present_situation_pattern_room,
                building_present_situation_pattern_hall=building_present_situation_pattern_hall,
                building_present_situation_pattern_health=building_present_situation_pattern_health,
                building_present_situation_pattern_compartmented=building_present_situation_pattern_compartmented,
                has_manages_organization=has_manages_organization,
                total_price=total_price,
                the_unit_price=the_unit_price,
                the_berth_category=the_berth_category,
                berth_shifting_total_area_square_meter=berth_shifting_total_area_square_meter,
                the_berth_total_price=the_berth_total_price,
                note=note,
                serial_number=serial_number,
                main_building_area=main_building_area,
                ancillary_building_area=ancillary_building_area,
                balcony_area=balcony_area,
                elevator=elevator,
                transfer_numder=transfer_numder)
            )
        
        realestate_data.objects.bulk_create(data_list)'''
        
        return Response("upload_data")
            