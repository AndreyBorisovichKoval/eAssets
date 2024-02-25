from datetime import datetime, timezone
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, request
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.models.TokenUser import username
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from typing import Any
from assets.api.serializers import (UserSerializer, DepartmentSerializer, DivisionSerializer, PositionSerializer,
                                    StaffSerializer, AssetTypeSerializer, AssetSerializer, AssetAssignmentSerializer)
from assets.models import *
import logging


# Получаем логгер Django
logger = logging.getLogger('django')
# logger = logging.getLogger(__name__)
# def my_function():
# logger.debug('user_id', get_user_id_from_token(request))
# logger.info('Это информационное сообщение')
# logger.warning('Это предупреждение')
# logger.error('Это сообщение об ошибке')
# logger.critical('Это критическое сообщение')


def get_user_id_from_token(request):
    try:
        authorization_header = request.headers.get('Authorization')
        access_token = AccessToken(authorization_header.split()[1])
        user_id = access_token['user_id']
        # logger.info(f'User: {user_id} добавлен в систему для доступа к ')
        return user_id
    except (AuthenticationFailed, IndexError):
        return None


@api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


class DepartmentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        # Добавляем запись о действии пользователя перед проверкой pk
        # action_description = f"User {request.user.username} initiated a GET request to retrieve department data."
        # UserAction.objects.create(user=request.user, action=action_description)

        if pk:
            try:
                department = Department.objects.get(pk=pk, is_deleted=False)
                serializer = DepartmentSerializer(department)
                logger.info(f"Department {department.id} {department.title} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Department.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the Department...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            departments = Department.objects.filter(is_deleted=False)
            serializer = DepartmentSerializer(departments, many=True)
            logger.info(f"All Departments viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def post(self, request):
        try:
            request.data['created_by'] = request.user.id
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                department = serializer.save()

                # Добавляем запись о действии пользователя с информацией о департаменте
                action_description = f"User {request.user.username} created a department: id = {department.id}, title = {department.title}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем добавление департамента
                logger.info(f"\n(__-=*=-__ Department {department.id} {department.title} added by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred while processing the POST request when creating the Department...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            department = Department.objects.get(pk=pk, is_deleted=False)
            serializer = DepartmentSerializer(department, data=request.data, partial=True)
            if serializer.is_valid():
                department = serializer.save()

                # Добавляем запись о действии пользователя с информацией о департаменте
                action_description = f"User {request.user.username} updated department: id = {department.id}, title = {department.title}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем обновление департамента
                logger.info(
                    f"\n(__-=*=-__ Department {department.id} {department.title} updated by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the PATCH request when updating the Department...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            department = Department.objects.get(pk=pk, is_deleted=False)
            department.deleted_by = request.user
            department.is_deleted = True
            department.save()

            # Заносим данные о действии пользователя
            action_description = f"User {request.user.username} deleted a department: id = {department.id}, title = {department.title}."
            UserAction.objects.create(user=request.user, action=action_description)

            # Логируем удаление департамента
            logger.info(f"\n(__-=*=-__ Department {department.id} {department.title} deleted by user {request.user.id} {request.user.username}. __-=*=-__)")

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the DELETE request when deleting the Department...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DivisionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                division = Division.objects.get(pk=pk, is_deleted=False)
                serializer = DivisionSerializer(division)
                logger.info(f"Division {division.id} {division.title} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Division.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the Division...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            divisions = Division.objects.filter(is_deleted=False)
            serializer = DivisionSerializer(divisions, many=True)
            logger.info(f"All Divisions viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def post(self, request):
        try:
            request.data['created_by'] = request.user.id
            serializer = DivisionSerializer(data=request.data)
            if serializer.is_valid():
                division = serializer.save()
                action_description = f"User {request.user.username} created a division: id = {division.id}, title = {division.title}."
                UserAction.objects.create(user=request.user, action=action_description)
                logger.info(
                    f"Division {division.id} {division.title} added by user {request.user.id} {request.user.username}.")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Department.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred while processing the POST request when creating the Division...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            division = Division.objects.get(pk=pk, is_deleted=False)
            department_id = request.data.get('department')
            department = Department.objects.get(pk=department_id)
            serializer = DivisionSerializer(division, data=request.data, partial=True)
            if serializer.is_valid():
                division = serializer.save()
                action_description = f"User {request.user.username} updated division: id = {division.id}, title = {division.title}."
                UserAction.objects.create(user=request.user, action=action_description)
                logger.info(f"Division {division.id} {division.title} updated by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Division.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the PATCH request when updating the Division...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            division = Division.objects.get(pk=pk, is_deleted=False)
            division.deleted_by = request.user
            division.is_deleted = True
            division.save()
            action_description = f"User {request.user.username} deleted a division: id = {division.id}, title = {division.title}."
            UserAction.objects.create(user=request.user, action=action_description)
            logger.info(f"Division {division.id} {division.title} deleted by user {request.user.id} {request.user.username}.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Division.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the DELETE request when deleting the Division...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PositionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        # Добавляем запись о действии пользователя перед проверкой pk
        # action_description = f"User {request.user.username} initiated a GET request to retrieve position data."
        # UserAction.objects.create(user=request.user, action=action_description)

        if pk:
            try:
                position = Position.objects.get(pk=pk, is_deleted=False)
                serializer = PositionSerializer(position)
                logger.info(f"Position {position.id} {position.title} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Position.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the Position...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            positions = Position.objects.filter(is_deleted=False)
            serializer = PositionSerializer(positions, many=True)
            logger.info(f"All Positions viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def post(self, request):
        try:
            request.data['created_by'] = request.user.id
            serializer = PositionSerializer(data=request.data)
            if serializer.is_valid():
                position = serializer.save()

                # Добавляем запись о действии пользователя с информацией о должности
                action_description = f"User {request.user.username} created a position: id = {position.id}, title = {position.title}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем добавление должности
                logger.info(f"\n(__-=*=-__ Position {position.id} {position.title} added by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred while processing the POST request when creating the Position...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            position = Position.objects.get(pk=pk, is_deleted=False)
            serializer = PositionSerializer(position, data=request.data, partial=True)
            if serializer.is_valid():
                position = serializer.save()

                # Добавляем запись о действии пользователя с информацией о должности
                action_description = f"User {request.user.username} updated position: id = {position.id}, title = {position.title}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем обновление должности
                logger.info(
                    f"\n(__-=*=-__ Position {position.id} {position.title} updated by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Position.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the PATCH request when updating the Position...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            position = Position.objects.get(pk=pk, is_deleted=False)
            position.deleted_by = request.user
            position.is_deleted = True
            position.save()

            # Заносим данные о действии пользователя
            action_description = f"User {request.user.username} deleted a position: id = {position.id}, title = {position.title}."
            UserAction.objects.create(user=request.user, action=action_description)

            # Логируем удаление должности
            logger.info(f"\n(__-=*=-__ Position {position.id} {position.title} deleted by user {request.user.id} {request.user.username}. __-=*=-__)")

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Position.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the DELETE request when deleting the Position...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StaffView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        # Добавляем запись о действии пользователя перед проверкой pk
        action_description = f"User {request.user.username} initiated a GET request to retrieve staff data."
        UserAction.objects.create(user=request.user, action=action_description)

        if pk:
            try:
                staff = Staff.objects.get(pk=pk, is_deleted=False)
                serializer = StaffSerializer(staff)
                logger.info(f"Staff {staff.id} {staff.name} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Staff.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the Staff...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            staff = Staff.objects.filter(is_deleted=False)
            serializer = StaffSerializer(staff, many=True)
            logger.info(f"All Staff viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def post(self, request):
        try:
            request.data['created_by'] = request.user.id
            serializer = StaffSerializer(data=request.data)
            if serializer.is_valid():
                staff = serializer.save()

                # Добавляем запись о действии пользователя с информацией о сотруднике
                action_description = f"User {request.user.username} created a staff member: id = {staff.id}, name = {staff.name}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем добавление сотрудника
                logger.info(f"\n(__-=*=-__ Staff {staff.id} {staff.name} added by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred while processing the POST request when creating the Staff...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            staff = Staff.objects.get(pk=pk, is_deleted=False)
            serializer = StaffSerializer(staff, data=request.data, partial=True)
            if serializer.is_valid():
                staff = serializer.save()

                # Добавляем запись о действии пользователя с информацией о сотруднике
                action_description = f"User {request.user.username} updated staff member: id = {staff.id}, name = {staff.name}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем обновление сотрудника
                logger.info(f"\n(__-=*=-__ Staff {staff.id} {staff.name} updated by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Staff.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the PATCH request when updating the Staff...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            staff = Staff.objects.get(pk=pk, is_deleted=False)
            staff.deleted_by = request.user
            staff.is_deleted = True
            staff.save()

            # Заносим данные о действии пользователя
            action_description = f"User {request.user.username} deleted a staff member: id = {staff.id}, name = {staff.name}."
            UserAction.objects.create(user=request.user, action=action_description)

            # Логируем удаление сотрудника
            logger.info(f"\n(__-=*=-__ Staff {staff.id} {staff.name} deleted by user {request.user.id} {request.user.username}. __-=*=-__)")

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Staff.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the DELETE request when deleting the Staff...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AssetTypeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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


class AssetAssignmentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
