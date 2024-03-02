import logging
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from assets.models import *
from assets.api.serializers import UserSerializer, UserSettingsSerializer


# Получаем логгер Django
logger = logging.getLogger('application')


# @api_view(["GET"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def get_user_settings(request):
#     user = request.user
#     try:
#         settings = UserSettings.objects.get(user=user)
#         serializer = UserSettingsSerializer(settings)
#         logger.info(f"User settings fetched for user: {user.username}")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except UserSettings.DoesNotExist:
#         logger.error(f"User settings not found for user: {user.username}")
#         return Response({'error': 'Settings not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST", "PATCH"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_settings(request):
    user = request.user
    try:
        settings = UserSettings.objects.get(user=user)

        if request.method == "GET":
            serializer = UserSettingsSerializer(settings)
            logger.info(f"Настройки пользователя получены для пользователя: {user.username}")
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serializer = UserSettingsSerializer(settings, data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Настройки пользователя добавлены для пользователя: {user.username}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                logger.error(f"Недопустимые данные для обновления настроек пользователя для пользователя: {user.username}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "PATCH":
            serializer = UserSettingsSerializer(settings, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Настройки пользователя обновлены для пользователя: {user.username}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                logger.error(f"Недопустимые данные для обновления настроек пользователя для пользователя: {user.username}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except UserSettings.DoesNotExist:
        logger.error(f"Настройки пользователя не найдены для пользователя: {user.username}")
        return Response({'error': 'Настройки не найдены'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_user(request):
    if not request.user.is_superuser:
        logger.warning("Only administrators can create users.")
        raise PermissionDenied("Only administrators can create users.")

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = request.user
        action = f"User '{serializer.data['username']}' created"
        user_action = UserAction(user=user, action=action)
        user_action.save()

        logger.info("User created successfully.")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        logger.error("Failed to create user.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
# @swagger_auto_schema(
#     operation_description="Просмотр всех пользователей",
#     responses={200: 'OK', 403: 'Нет доступа'}
# )
def view_users(request):
    if not request.user.is_superuser:
        logger.warning("Only administrators can view users.")
        raise PermissionDenied("Only administrators can view users.")

    # Логика для просмотра пользователей
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    # Проверяем, является ли пользователь аутентифицированным
    if not user.is_authenticated:
        logger.warning("User is not authenticated.")
        raise PermissionDenied("User is not authenticated.")
    # Получаем текущий пароль пользователя
    current_password = request.data.get("current_password")
    # Проверяем, совпадает ли текущий пароль с паролем пользователя
    if not user.check_password(current_password):
        logger.warning("Current password is incorrect.")
        raise PermissionDenied("Current password is incorrect.")
    # Получаем новый пароль
    new_password = request.data.get("new_password")
    # Устанавливаем новый пароль для пользователя
    user.password = make_password(new_password)
    user.save()

    action = f"Password changed for user '{user.username}'"
    user_action = UserAction(user=user, action=action)
    user_action.save()

    logger.info("Password changed successfully.")
    return Response("Password changed successfully.", status=status.HTTP_200_OK)

