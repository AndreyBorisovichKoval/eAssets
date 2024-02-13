from django.urls import path
from assets.api.views import AssetViewSet, AssetDetail


urlpatterns = [
    path('assets/', AssetViewSet.as_view(), name='assets-list'),
    path('assets/<int:pk>/', AssetDetail.as_view(), name='assets-detail'),
]

# urlpatterns = [
#     path('assets/', AssetViewSet.as_view(), name='assets-list'),
#     path('assets/<int:id>/', AssetDetail.as_view(), name='assets-detail'),
#     # path('assets/<int:id>/details/', AssetDetailWithDetails.as_view(), name='assets-detail-with-details'),
# ]


"""
[GET] /tasks
[POST] /tasks

[PUT] /tasks/<int:id>
[DELETE] /tasks/<int:id>

[GET] /tasks/<int:id>/details
"""
