from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from typing import Any
from assets.api.serializers import (UserSerializer, AssetSerializer, DepartmentSerializer, DivisionSerializer,
                                    PositionSerializer, AssetTypeSerializer, StaffSerializer, AssetAssignmentSerializer)
from assets.models import *
# from assets.models import Asset
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


class DepartmentView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            departments = Department.objects.filter(is_deleted=False)
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data)
        else:
            try:
                department = Department.objects.get(pk=pk, is_deleted=False)
                serializer = DepartmentSerializer(department)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Department.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            department = Department.objects.get(pk=pk, is_deleted=False)
            serializer = DepartmentSerializer(department, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            department = Department.objects.get(pk=pk, is_deleted=False)
            serializer = DepartmentSerializer(department, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            department = Department.objects.get(pk=pk, is_deleted=False)
            department.is_deleted = True
            # department.delete()
            department.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DivisionView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            divisions = Division.objects.filter(is_deleted=False)
            serializer = DivisionSerializer(divisions, many=True)
            return Response(serializer.data)
        else:
            try:
                division = Division.objects.get(pk=pk, is_deleted=False)
                serializer = DivisionSerializer(division)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Division.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = DivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            division = Division.objects.get(pk=pk, is_deleted=False)
            serializer = DivisionSerializer(division, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Division.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            division = Division.objects.get(pk=pk, is_deleted=False)
            serializer = DivisionSerializer(division, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Division.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            division = Division.objects.get(pk=pk, is_deleted=False)
            division.is_deleted = True
            division.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Division.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PositionView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            positions = Position.objects.filter(is_deleted=False)
            serializer = PositionSerializer(positions, many=True)
            return Response(serializer.data)
        else:
            try:
                position = Position.objects.get(pk=pk, is_deleted=False)
                serializer = PositionSerializer(position)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Position.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            position = Position.objects.get(pk=pk, is_deleted=False)
            serializer = PositionSerializer(position, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Position.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            position = Position.objects.get(pk=pk, is_deleted=False)
            serializer = PositionSerializer(position, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Position.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            position = Position.objects.get(pk=pk, is_deleted=False)
            position.is_deleted = True
            position.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Position.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AssetTypeView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            asset_types = AssetType.objects.filter(is_deleted=False)
            serializer = AssetTypeSerializer(asset_types, many=True)
            return Response(serializer.data)
        else:
            try:
                asset_type = AssetType.objects.get(pk=pk, is_deleted=False)
                serializer = AssetTypeSerializer(asset_type)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except AssetType.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AssetTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            asset_type = AssetType.objects.get(pk=pk, is_deleted=False)
            serializer = AssetTypeSerializer(asset_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AssetType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            asset_type = AssetType.objects.get(pk=pk, is_deleted=False)
            serializer = AssetTypeSerializer(asset_type, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AssetType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            asset_type = AssetType.objects.get(pk=pk, is_deleted=False)
            asset_type.is_deleted = True
            asset_type.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AssetType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AssetView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get_object(self, pk):
    #     try:
    #         return Asset.objects.get(pk=pk)
    #     except Asset.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        if pk is None:
            asset = Asset.objects.all()
            serializer = AssetSerializer(asset, many=True)
            return Response(serializer.data)
        else:
            try:
                asset = Asset.objects.get(pk=pk)
                serializer = AssetSerializer(asset)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Asset.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request: Any) -> Any:
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request: Any, pk: int) -> Any:
        try:
            asset = Asset.objects.get(pk=pk)
            serializer = AssetSerializer(asset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Asset.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def patch(self, request: Any, pk: int) -> Any:
        try:
            asset = Asset.objects.get(pk=pk)
            serializer = AssetSerializer(asset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Asset.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Any, pk: int) -> Any:
        try:
            asset = Asset.objects.get(pk=pk)
            asset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Asset.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class StaffView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            staff_members = Staff.objects.filter(is_deleted=False)
            serializer = StaffSerializer(staff_members, many=True)
            return Response(serializer.data)
        else:
            try:
                staff_member = Staff.objects.get(pk=pk, is_deleted=False)
                serializer = StaffSerializer(staff_member)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Staff.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            staff_member = Staff.objects.get(pk=pk, is_deleted=False)
            serializer = StaffSerializer(staff_member, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Staff.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            staff_member = Staff.objects.get(pk=pk, is_deleted=False)
            serializer = StaffSerializer(staff_member, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Staff.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            staff_member = Staff.objects.get(pk=pk, is_deleted=False)
            staff_member.is_deleted = True
            staff_member.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Staff.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AssetAssignmentView(APIView):
    def post(self, request):
        serializer = AssetAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            assignment = AssetAssignment.objects.get(pk=pk)
            assignment.return_date = request.data['return_date']
            assignment.save()
            return Response({'message': 'Return date updated successfully.'})
        except AssetAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


