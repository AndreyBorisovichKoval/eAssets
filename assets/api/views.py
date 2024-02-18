from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from typing import Any
from rest_framework_simplejwt.tokens import AccessToken
from assets.api.serializers import AssetSerializer
from assets.models import Asset
# from suppress import suppress
# @suppress


def get_user_id_from_token(request):
    try:
        authorization_header = request.headers.get('Authorization')
        access_token = AccessToken(authorization_header.split()[1])
        user_id = access_token['user_id']
        return user_id
    except (AuthenticationFailed, IndexError):
        return None


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()


class AssetView(APIView):
    def get(self, request: Any) -> Any:
        assets_data = Asset.objects.all()
        serializer = AssetSerializer(assets_data, many=True)
        return Response(serializer.data)
        # return Response(serializer.data, status=200)


# class AssetViewSet(APIView):
#     def get(self, request: Any) -> Any:
#         assets_data = Asset.objects.all()
#         serializer = AssetSerializer(assets_data, many=True)
#         return Response(serializer.data)
#         # return Response(serializer.data, status=200)
#
#     def post(self, request: Any) -> Any:
#         serializer = AssetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AssetDetail(APIView):
#     # def get_object(self, pk):
#     #     return get_object_or_404(Task, pk=pk)
#     def get(self, request: Any, pk: int) -> Any:
#         try:
#             asset = Asset.objects.get(pk=pk)
#             serializer = AssetSerializer(asset)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Asset.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request: Any, pk: int) -> Any:
#         try:
#             asset = Asset.objects.get(pk=pk)
#             serializer = AssetSerializer(asset, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Asset.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     def patch(self, request: Any, pk: int) -> Any:
#         try:
#             asset = Asset.objects.get(pk=pk)
#             serializer = AssetSerializer(asset, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Asset.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request: Any, pk: int) -> Any:
#         try:
#             asset = Asset.objects.get(pk=pk)
#             asset.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Asset.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
