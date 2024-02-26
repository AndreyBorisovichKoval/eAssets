from django.urls import path
# from assets.api.views import AssetViewSet, AssetDetail
from assets.api.views import (DepartmentView, DivisionView, PositionView, StaffView, AssetTypeView, AssetView,
                              AssetAssignmentView)
from assets.api.views_reports import *


urlpatterns = [
    path('department/', DepartmentView.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentView.as_view(), name='department-detail'),

    path('division/', DivisionView.as_view(), name='division-list'),
    path('division/<int:pk>/', DivisionView.as_view(), name='division-detail'),

    path('position/', PositionView.as_view(), name='position-list'),
    path('position/<int:pk>/', PositionView.as_view(), name='position-detail'),

    path('staff/', StaffView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffView.as_view(), name='staff-detail'),

    path('assettype/', AssetTypeView.as_view(), name='assettype-list'),
    path('assettype/<int:pk>/', AssetTypeView.as_view(), name='assettype-detail'),

    path('asset/', AssetView.as_view(), name='asset-list'),
    path('asset/<int:pk>/', AssetView.as_view(), name='asset-detail'),
    path('asset/written_off/', AssetView.as_view(), name='asset-list'),
    path('asset/written_off/<int:pk>/', AssetView.as_view(), name='asset-list'),

    path('assetassignment/', AssetAssignmentView.as_view(), name='assetassignment-list'),
    path('assetassignment/<int:pk>/', AssetAssignmentView.as_view(), name='assetassignment-detail'),

    path('reports/staff/<int:pk>/assets/', get_staff_assets, name='staff_assets-list'),
    path('reports/department/<int:pk>/assets/', get_department_assets, name='department_assets-list'),
    path('reports/division/<int:pk>/assets/', get_division_assets, name='division_assets-list'),
    path('reports/retired_assets/', get_retired_assets, name='retired_assets-list'),
    path('reports/cost_assets/', calculate_cost_assets, name='calculate_cost_assets-list'),
    path('reports/current_cost_assets/', calculate_current_cost_assets, name='calculate_current_cost_assets-list'),

]



"""
[GET] /tasks
[POST] /tasks

[PUT] /tasks/<int:id>
[DELETE] /tasks/<int:id>

[GET] /tasks/<int:id>/details
"""
