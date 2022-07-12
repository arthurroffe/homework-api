# Generated by Django 3.1.5 on 2022-07-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='realestate_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_district', models.CharField(max_length=200)),
                ('transaction_sign', models.CharField(max_length=200)),
                ('number_plate', models.CharField(max_length=200)),
                ('area_square_meter', models.CharField(max_length=200)),
                ('use_zoning', models.CharField(max_length=200)),
                ('non_metropolis', models.CharField(blank=True, max_length=200)),
                ('non_metropolis_use', models.CharField(blank=True, max_length=200)),
                ('transaction_date', models.CharField(max_length=200)),
                ('transaction_pen_number', models.CharField(max_length=200)),
                ('shifting_level', models.CharField(max_length=200)),
                ('total_floor', models.CharField(max_length=200)),
                ('building_state', models.CharField(blank=True, max_length=200)),
                ('main_use', models.CharField(blank=True, max_length=200)),
                ('main_building_material', models.CharField(blank=True, max_length=200)),
                ('construction_complete_year', models.CharField(blank=True, max_length=200)),
                ('building_shifting_total_area', models.CharField(blank=True, max_length=200)),
                ('building_present_situation_pattern_room', models.CharField(max_length=200)),
                ('building_present_situation_pattern_hall', models.CharField(max_length=200)),
                ('building_present_situation_pattern_health', models.CharField(max_length=200)),
                ('building_present_situation_pattern_compartmented', models.CharField(max_length=200)),
                ('has_manages_organization', models.CharField(max_length=200)),
                ('total_price', models.CharField(max_length=200)),
                ('the_unit_price', models.IntegerField(blank=True)),
                ('the_berth_category', models.CharField(blank=True, max_length=200)),
                ('berth_shifting_total_area_square_meter', models.FloatField()),
                ('the_berth_total_price', models.IntegerField()),
                ('note', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(max_length=200)),
                ('main_building_area', models.FloatField()),
                ('ancillary_building_area', models.FloatField()),
                ('balcony_area', models.FloatField()),
                ('elevator', models.CharField(blank=True, max_length=200)),
                ('transfer_numder', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]