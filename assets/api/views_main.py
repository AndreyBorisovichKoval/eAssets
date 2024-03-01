import logging
from datetime import datetime

from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from assets.models import *
from assets.api.serializers import (
    DepartmentSerializer,
    DivisionSerializer,
    PositionSerializer,
    StaffSerializer,
    AssetTypeSerializer,
    AssetSerializer,
    AssetAssignmentSerializer,
)

# Получаем логгер Django
logger = logging.getLogger('django')


class DepartmentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):

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
            department.deleted_at = datetime.now()
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
            division.deleted_at = datetime.now()
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
            position.deleted_at = datetime.now()
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
        # action_description = f"User {request.user.username} initiated a GET request to retrieve staff data."
        # UserAction.objects.create(user=request.user, action=action_description)

        if pk:
            try:
                staff_members = Staff.objects.get(pk=pk, is_deleted=False)
                serializer = StaffSerializer(staff_members)
                logger.info(f"Staff {staff_members.id} {staff_members.full_name} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Staff.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the Staff...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            staff_members = Staff.objects.filter(is_deleted=False)
            serializer = StaffSerializer(staff_members, many=True)
            logger.info(f"All Staff viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def post(self, request):
        try:
            request.data['created_by'] = request.user.id
            serializer = StaffSerializer(data=request.data)
            if serializer.is_valid():
                staff_members = serializer.save()

                # Добавляем запись о действии пользователя с информацией о сотруднике
                action_description = f"User {request.user.username} created a staff member: id = {staff_members.id}, full_name = {staff_members.full_name}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем добавление сотрудника
                logger.info(f"\n(__-=*=-__ Staff {staff_members.id} {staff_members.full_name} added by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred while processing the POST request when creating the Staff...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            staff_members = Staff.objects.get(pk=pk, is_deleted=False)
            serializer = StaffSerializer(staff_members, data=request.data, partial=True)
            if serializer.is_valid():
                staff_members = serializer.save()

                # Добавляем запись о действии пользователя с информацией о сотруднике
                action_description = f"User {request.user.username} updated staff member: id = {staff_members.id}, full_name = {staff_members.full_name}, division = {staff_members.division}, position = {staff_members.position}, memo = {staff_members.memo}."
                UserAction.objects.create(user=request.user, action=action_description)

                # Логируем обновление сотрудника
                logger.info(f"\n(__-=*=-__ Staff {staff_members.id} {staff_members.full_name} updated by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Staff.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the PATCH request when updating the Staff...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            staff_members = Staff.objects.get(pk=pk, is_deleted=False)
            staff_members.deleted_by = request.user
            staff_members.is_deleted = True
            staff_members.deleted_at = datetime.now()
            staff_members.save()

            # Заносим данные о действии пользователя
            action_description = f"User {request.user.username} deleted a staff member: id = {staff_members.id}, full_name = {staff_members.full_name}."
            UserAction.objects.create(user=request.user, action=action_description)

            # Логируем удаление сотрудника
            logger.info(f"\n(__-=*=-__ Staff {staff_members.id} {staff_members.full_name} deleted by user {request.user.id} {request.user.username}. __-=*=-__)")

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
        if pk:
            try:
                asset_type = AssetType.objects.get(pk=pk, is_deleted=False)
                serializer = AssetTypeSerializer(asset_type)
                logger.info(f"AssetType {asset_type.id} {asset_type.title} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except AssetType.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the AssetType...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            asset_types = AssetType.objects.filter(is_deleted=False)
            serializer = AssetTypeSerializer(asset_types, many=True)
            logger.info(f"All AssetTypes viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def post(self, request):
        try:
            request.data['created_by'] = request.user.id
            serializer = AssetTypeSerializer(data=request.data)
            if serializer.is_valid():
                asset_type = serializer.save()

                action_description = f"User {request.user.username} created an asset type: id = {asset_type.id}, title = {asset_type.title}."
                UserAction.objects.create(user=request.user, action=action_description)

                logger.info(f"\n(__-=*=-__ AssetType {asset_type.id} {asset_type.title} added by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred while processing the POST request when creating the AssetType...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            asset_type = AssetType.objects.get(pk=pk, is_deleted=False)
            serializer = AssetTypeSerializer(asset_type, data=request.data, partial=True)
            if serializer.is_valid():
                asset_type = serializer.save()

                action_description = f"User {request.user.username} updated asset type: id = {asset_type.id}, title = {asset_type.title}."
                UserAction.objects.create(user=request.user, action=action_description)

                logger.info(
                    f"\n(__-=*=-__ AssetType {asset_type.id} {asset_type.title} updated by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AssetType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the PATCH request when updating the AssetType...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            asset_type = AssetType.objects.get(pk=pk, is_deleted=False)
            asset_type.deleted_by = request.user
            asset_type.is_deleted = True
            asset_type.deleted_at = datetime.now()
            asset_type.save()

            action_description = f"User {request.user.username} deleted an asset type: id = {asset_type.id}, title = {asset_type.title}."
            UserAction.objects.create(user=request.user, action=action_description)

            logger.info(f"\n(__-=*=-__ AssetType {asset_type.id} {asset_type.title} deleted by user {request.user.id} {request.user.username}. __-=*=-__)")

            return Response(status=status.HTTP_204_NO_CONTENT)
        except AssetType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the DELETE request when deleting the AssetType...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AssetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                asset = Asset.objects.get(pk=pk, is_written_off=False)
                serializer = AssetSerializer(asset)
                logger.info(f"Asset {asset.id} {asset.title} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Asset.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the Asset...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            assets = Asset.objects.filter(is_written_off=False)
            serializer = AssetSerializer(assets, many=True)
            logger.info(f"All Assets viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def post(self, request):
        try:
            request.data['created_by'] = request.user.id
            serializer = AssetSerializer(data=request.data)
            if serializer.is_valid():
                asset = serializer.save()

                action_description = f"User {request.user.username} created an asset: id = {asset.id}, title = {asset.title}, inventory_number = {asset.inventory_number}, identifier = {asset.identifier}, acquisition_date = {asset.acquisition_date}, service_life = {asset.service_life}, cost = {asset.cost}, service_life = {asset.service_life}, description = {asset.description}, asset_type = {asset.asset_type}."
                UserAction.objects.create(user=request.user, action=action_description)

                logger.info(f"\n(__-=*=-__ Asset {asset.id} {asset.title} added by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred while processing the POST request when creating the Asset...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            asset = Asset.objects.get(pk=pk, is_written_off=False)
            serializer = AssetSerializer(asset, data=request.data, partial=True)
            if serializer.is_valid():
                asset = serializer.save()

                action_description = f"User {request.user.username} updated asset: id = {asset.id}, title = {asset.title}, inventory_number = {asset.inventory_number}, identifier = {asset.identifier}, acquisition_date = {asset.acquisition_date}, service_life = {asset.service_life}, cost = {asset.cost}, service_life = {asset.service_life}, description = {asset.description}, asset_type = {asset.asset_type}."
                UserAction.objects.create(user=request.user, action=action_description)

                logger.info(
                    f"\n(__-=*=-__ Asset {asset.id} {asset.title} updated by user {request.user.id} {request.user.username}. __-=*=-__)")

                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Asset.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the PATCH request when updating the Asset...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk=None):
        if pk:
            try:
                asset = Asset.objects.get(pk=pk, is_written_off=True)
                serializer = AssetSerializer(asset)
                logger.info(f"Asset {asset.id} {asset.title} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Asset.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request when retrieving the Asset...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            assets = Asset.objects.filter(is_written_off=True)
            serializer = AssetSerializer(assets, many=True)
            logger.info(f"All Assets viewed by user {request.user.id} {request.user.username}.")
            return Response(serializer.data)

    def delete(self, request, pk):
        try:
            asset = Asset.objects.get(pk=pk, is_written_off=False)
            asset.written_off_by = request.user
            asset.is_written_off = True
            asset.written_off_at = datetime.now()
            asset.save()

            action_description = f"User {request.user.username} wrote off fixed asset: id = {asset.id}, title = {asset.title}."
            UserAction.objects.create(user=request.user, action=action_description)

            logger.info(f"\n(__-=*=-__ Asset {asset.id} {asset.title} deleted by user {request.user.id} {request.user.username}. __-=*=-__)")

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Asset.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the DELETE request when deleting the Asset...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class AssetAssignmentView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         serializer = AssetAssignmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         try:
#             assignment = AssetAssignment.objects.get(pk=pk)
#             assignment.return_date = request.data['return_date']
#             assignment.save()
#             return Response({'message': 'Return date updated successfully.'})
#         except AssetAssignment.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)


class AssetAssignmentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                asset_assignment = AssetAssignment.objects.get(pk=pk)
                serializer = AssetAssignmentSerializer(asset_assignment)
                logger.info(f"AssetAssignment {asset_assignment.id} viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except AssetAssignment.DoesNotExist:
                logger.error(f"AssetAssignment with pk={pk} does not exist")
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request for asset assignment...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            try:
                asset_assignments = AssetAssignment.objects.all()
                serializer = AssetAssignmentSerializer(asset_assignments, many=True)
                logger.info(f"All AssetsAssignments viewed by user {request.user.id} {request.user.username}.")
                return Response(serializer.data)
            except Exception as e:
                logger.exception("An error occurred while processing the GET request for asset assignments...")
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = AssetAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Устанавливаем assignment_by в текущего пользователя
                serializer.validated_data['assignment_by'] = request.user

                asset_assignment = serializer.save()

                action_description = f"User {request.user.id} {request.user.username} created asset assignment: {asset_assignment.id}. The fixed asset {asset_assignment.asset} is tied to the employee {asset_assignment.staff}."

                # Создаем запись в UserAction
                UserAction.objects.create(user=request.user, action=action_description)

                logger.info(f"\n(__-=*=-__ {action_description} __-=*=-__)")

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f"Error creating asset assignment: {str(e)}")
                return Response("Error creating asset assignment.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger.error(f"Invalid asset assignment data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            asset_assignment = AssetAssignment.objects.get(pk=pk)
            asset_assignment.return_date = datetime.now().date()
            asset_assignment.return_by = request.user
            asset_assignment.save()

            action_description = f"User {request.user.username} updated return date for asset assignment: id = {asset_assignment.id}, asset = {asset_assignment.asset}, staff = {asset_assignment.staff}."
            UserAction.objects.create(user=request.user, action=action_description)

            logger.info(f"\n(__-=*=-__ {action_description} __-=*=-__)")

            return Response({'message': 'Return date updated successfully.'})
        except AssetAssignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred while processing the DELETE request when updating return date for the asset assignment...")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def move_asset_assignment(self, request, pk):
    def patch(self, request, pk):

        delete_response = self.delete(request, pk)
        post_response = self.post(request)
        return post_response
