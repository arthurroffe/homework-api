from django.db import models

# Create your models here.
class realestate_data(models.Model):
    the_district = models.CharField(max_length=200,blank=True)
    transaction_sign = models.CharField(max_length=200,blank=True)
    number_plate = models.CharField(max_length=200,blank=True)
    area_square_meter = models.CharField(max_length=200,blank=True)
    use_zoning = models.CharField(max_length=200,blank=True)
    non_metropolis = models.CharField(max_length=200,blank=True)
    non_metropolis_use = models.CharField(max_length=200,blank=True)
    transaction_date = models.CharField(max_length=200,blank=True)
    transaction_pen_number = models.CharField(max_length=200,blank=True)
    shifting_level = models.CharField(max_length=200,blank=True)
    total_floor = models.CharField(max_length=200,blank=True)
    building_state = models.CharField(max_length=200,blank=True)
    main_use = models.CharField(max_length=200,blank=True)
    main_building_material = models.CharField(max_length=200,blank=True)
    construction_complete_year = models.CharField(max_length=200,blank=True)
    building_shifting_total_area = models.CharField(max_length=200,blank=True)
    building_present_situation_pattern_room = models.CharField(max_length=200,blank=True)
    building_present_situation_pattern_hall = models.CharField(max_length=200,blank=True)
    building_present_situation_pattern_health = models.CharField(max_length=200,blank=True)
    building_present_situation_pattern_compartmented = models.CharField(max_length=200,blank=True)
    has_manages_organization = models.CharField(max_length=200,blank=True)
    total_price = models.CharField(max_length=200,blank=True)
    the_unit_price = models.CharField(max_length=200,blank=True)
    the_berth_category = models.CharField(max_length=200,blank=True)
    berth_shifting_total_area_square_meter = models.FloatField(blank=True)
    the_berth_total_price = models.IntegerField(blank=True)
    note = models.CharField(max_length=200,blank=True)
    serial_number = models.CharField(max_length=200,blank=True)
    main_building_area = models.FloatField(blank=True)
    ancillary_building_area = models.FloatField(blank=True)
    balcony_area = models.FloatField(blank=True)
    elevator = models.CharField(max_length=200,blank=True)
    transfer_numder = models.CharField(max_length=200,blank=True)
    
class realestate_data_2(models.Model):
    the_district = models.CharField(max_length=200,blank=True)
    total_floor = models.CharField(max_length=200,blank=True)
    building_state = models.CharField(max_length=200,blank=True)
    
    