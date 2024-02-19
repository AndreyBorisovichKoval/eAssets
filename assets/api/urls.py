from django.urls import path
# from assets.api.views import AssetViewSet, AssetDetail
from assets.api.views import (DepartmentView, DivisionView, PositionView, StaffView, AssetTypeView, AssetView,
                              AssetAssignmentView)


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
    path('assetassignment/', AssetAssignmentView.as_view(), name='assetassignment-list'),
    path('assetassignment/<int:pk>/', AssetAssignmentView.as_view(), name='assetassignment-detail'),
]



"""
[GET] /tasks
[POST] /tasks

[PUT] /tasks/<int:id>
[DELETE] /tasks/<int:id>

[GET] /tasks/<int:id>/details
"""
