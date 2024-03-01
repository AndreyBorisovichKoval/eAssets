import logging
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import pandas as pd
from assets.models import *

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


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def calculate_total_price_by_type(request, pk):
    total_price = Asset.objects.filter(asset_type_id=pk, is_written_off=False).aggregate(Sum('cost'))['cost__sum']
    if total_price is None:
        total_price = 0

    logger.info(f"Calculated total price for asset type with id {pk}")
    return JsonResponse({'total_price': total_price}, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def calculate_current_price_by_type(request, pk):
    current_price = Asset.objects.filter(asset_type_id=pk, is_written_off=False).aggregate(Sum('current_cost'))['current_cost__sum']
    if current_price is None:
        current_price = 0

    logger.info(f"Calculated current price for asset type with id {pk}")
    return JsonResponse({'current_price': current_price}, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def export_to_xlsx(request):
    assets = Asset.objects.all().values(
        'inventory_number',
        'title',
        'identifier',
        'acquisition_date',
        'service_life',
        'cost',
        'current_cost',
        'last_recalculation_date',
        'description',
        'asset_type',
        'is_written_off',
        'written_off_at'
    )
    assignments = AssetAssignment.objects.select_related('asset', 'staff').all().values(
        'asset',
        'staff',
        'assignment_date',
        'return_date'
    )
    staff = Staff.objects.select_related('division', 'position').all().values(
        'last_name',
        'first_name',
        'patronymic',
        'division__department',
        'division__title',
        'position'
    )
    divisions = Division.objects.select_related('department').all().values(
        'department__title',
        'title'
    )
    departments = Department.objects.all().values(
        'title'
    )

    assets_df = pd.DataFrame(list(assets))
    assignments_df = pd.DataFrame(list(assignments))
    staff_df = pd.DataFrame(list(staff))
    divisions_df = pd.DataFrame(list(divisions))
    departments_df = pd.DataFrame(list(departments))

    # Преобразование объектов datetime в строки без информации о часовом поясе
    assets_df['acquisition_date'] = assets_df['acquisition_date'].apply(lambda dt: dt.strftime('%Y-%m-%d') if pd.notnull(dt) else None)
    assignments_df['assignment_date'] = assignments_df['assignment_date'].apply(lambda dt: dt.strftime('%Y-%m-%d') if pd.notnull(dt) else None)
    assignments_df['return_date'] = assignments_df['return_date'].apply(lambda dt: dt.strftime('%Y-%m-%d') if pd.notnull(dt) else None)
    assets_df['last_recalculation_date'] = assets_df['last_recalculation_date'].apply(lambda dt: dt.strftime('%Y-%m-%d') if pd.notnull(dt) else None)
    assets_df['written_off_at'] = assets_df['written_off_at'].apply(lambda dt: dt.strftime('%Y-%m-%d') if pd.notnull(dt) else None)

    # Создание книги Excel с форматом .xlsx
    with pd.ExcelWriter('additional/Reports/report.xlsx', engine='xlsxwriter') as writer:
        assets_df.to_excel(writer, sheet_name='Assets', index=False)
        assignments_df.to_excel(writer, sheet_name='Assignments', index=False)
        staff_df.to_excel(writer, sheet_name='Staff', index=False)
        divisions_df.to_excel(writer, sheet_name='Divisions', index=False)
        departments_df.to_excel(writer, sheet_name='Departments', index=False)

    # Закрытие объекта ExcelWriter и сохранение файла .xlsx
    writer.close()

    # Отправка файла .xlsx в ответе HTTP
    with open('additional/Reports/report.xlsx', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=additional/Reports/report.xlsx'
        return response


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def export_to_xlsx_report(request):
    assets = Asset.objects.all().values(
        'inventory_number',
        'title',
        'identifier',
        'acquisition_date',
        'service_life',
        'cost',
        'current_cost',
        'last_recalculation_date',
        'description',
        'asset_type__title',
        'is_written_off',
        'written_off_at'
    )

    assignments = AssetAssignment.objects.select_related('asset', 'staff').all().values(
        'asset__inventory_number',
        'staff_id',
        'assignment_date',
        'return_date'
    )

    staff = Staff.objects.select_related('division', 'position').all().values(
        'id',
        'last_name',
        'first_name',
        'patronymic',
        'division__department__title',
        'division__title',
        'position_id',
        'position__title'
    )

    assets_df = pd.DataFrame(list(assets))
    assignments_df = pd.DataFrame(list(assignments))
    staff_df = pd.DataFrame(list(staff))

    assets_df.columns = [
        'inventory_number',
        'title',
        'identifier',
        'acquisition_date',
        'service_life',
        'cost',
        'current_cost',
        'last_recalculation_date',
        'description',
        'asset_type',
        'is_written_off',
        'written_off_at'
    ]

    assignments_df.columns = [
        'inventory_number',
        'staff_id',
        'assignment_date',
        'return_date'
    ]

    staff_df.columns = [
        'staff_id',
        'last_name',
        'first_name',
        'patronymic',
        'division_department',
        'division_title',
        'position_id',
        'position_title'
    ]

    assets_df['acquisition_date'] = pd.to_datetime(assets_df['acquisition_date']).dt.date.astype(str)
    assignments_df['assignment_date'] = pd.to_datetime(assignments_df['assignment_date']).dt.date.astype(str)
    assignments_df['return_date'] = pd.to_datetime(assignments_df['return_date']).dt.date.astype(str)
    assets_df['last_recalculation_date'] = pd.to_datetime(assets_df['last_recalculation_date']).dt.date.astype(str)
    assets_df['written_off_at'] = pd.to_datetime(assets_df['written_off_at']).dt.date.astype(str)

    # combined_df = assets_df.merge(assignments_df, left_on='inventory_number', right_on='inventory_number', how='left')
    # combined_df = combined_df.merge(staff_df, left_on='staff_id', right_on='staff_id', how='left')

    combined_df = assets_df.merge(
        right=assignments_df,
        on='inventory_number',
        how='left'
    ).merge(
        right=staff_df,
        on='staff_id',
        how='left'
    )

    # Создание книги Excel с форматом .xlsx
    writer = pd.ExcelWriter('additional/Reports/report_in_one_sheets.xlsx', engine='xlsxwriter')
    combined_df.to_excel(writer, sheet_name='Combined', index=False)

    # Получение объекта xlsxwriter.Workbook и листа
    workbook = writer.book
    worksheet = writer.sheets['Combined']

    # Вставка столбца 'position_title' рядом со столбцом 'position'
    worksheet.write(0, combined_df.columns.get_loc('position_id') + 1, 'position_title')

    # Закрытие объекта ExcelWriter и сохранение файла .xlsx
    writer.close()

    # Отправка файла .xlsx в ответе HTTP
    with open('additional/Reports/report_in_one_sheets.xlsx', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=additional/Reports/report_in_one_sheets.xlsx'
        return response
