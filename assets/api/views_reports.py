from datetime import datetime, timezone
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status, viewsets, request
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.models.TokenUser import username
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from typing import Any
from assets.api.serializers import (UserSerializer, DepartmentSerializer, DivisionSerializer, PositionSerializer,
                                    StaffSerializer, AssetTypeSerializer, AssetSerializer, AssetAssignmentSerializer)
from assets.models import *
import logging

logger = logging.getLogger('django')


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_staff_assets(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    assigned_assets = Asset.objects.filter(assetassignment__staff=staff)

    asset_list = []
    for asset in assigned_assets:
        asset_list.append({
            'asset_type': asset.asset_type.title if asset.asset_type else None,
            'inventory_number': asset.inventory_number,
            'title': asset.title,
            'identifier': asset.identifier,
        })

    logger.info(f"__-=*=-__ Retrieved assigned assets for staff with ID: {pk}. __-=*=-__")
    return JsonResponse(asset_list, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_department_assets(request, pk):
    department = get_object_or_404(Department, id=pk)
    staff_in_department = Staff.objects.filter(division__department=department)
    assigned_assets = Asset.objects.filter(assetassignment__staff__in=staff_in_department)

    asset_list = []
    for asset in assigned_assets:
        asset_list.append({
            'asset_type': asset.asset_type.title if asset.asset_type else None,
            'inventory_number': asset.inventory_number,
            'title': asset.title,
            'identifier': asset.identifier,
        })

    logger.info(f"Retrieved assets for department with ID: {pk}")
    return JsonResponse(asset_list, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_division_assets(request, pk):
    division = get_object_or_404(Division, id=pk)
    staff_in_division = Staff.objects.filter(division=division)
    assigned_assets = Asset.objects.filter(assetassignment__staff__in=staff_in_division)

    asset_list = []
    for asset in assigned_assets:
        asset_assignments = asset.assetassignment_set.all()
        staff_full_names = [assignment.staff.full_name for assignment in asset_assignments]

        asset_list.append({
            'division': division.title,
            'staff_full_names': staff_full_names,
            'asset_type': asset.asset_type.title if asset.asset_type else None,
            'inventory_number': asset.inventory_number,
            'title': asset.title,
            'identifier': asset.identifier,
        })

    logger.info(f"Retrieved assets for division with ID: {pk}")
    return JsonResponse(asset_list, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_retired_assets(request):
    retired_assets = Asset.objects.filter(is_written_off=True)

    asset_list = []
    for asset in retired_assets:
        asset_list.append({
            'asset_type': asset.asset_type.title if asset.asset_type else None,
            'inventory_number': asset.inventory_number,
            'title': asset.title,
            'identifier': asset.identifier,
        })

    logger.info("Retrieved retired assets")
    return JsonResponse(asset_list, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def calculate_cost_assets(request):
    total_price = Asset.objects.filter(is_written_off=False).aggregate(Sum('cost'))['cost__sum']
    if total_price is None:
        total_price = 0

    logger.info("Calculated total price of active assets")
    return JsonResponse({'total_price': total_price}, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def calculate_current_cost_assets(request):
    total_price = Asset.objects.filter(is_written_off=False).aggregate(Sum('current_cost'))['current_cost__sum']
    if total_price is None:
        total_price = 0

    logger.info("Calculated total current price of active assets")
    return JsonResponse({'total_current_price': total_price}, safe=False)
