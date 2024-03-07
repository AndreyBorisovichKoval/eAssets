"""
URL configuration for eAssets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# from django.core.mail import send_mail
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from additional.email_sender import send_email
from assets.api.views.user import view_users, create_user, change_password, get_user_settings, create_user_settings, update_user_settings
from assets.views import recalculate_assets_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('assets/', include('assets.urls')),

    path('auth/view_users/', view_users, name='sign-up'),
    path('auth/sign-up/', create_user, name='sign-up'),

    path('auth/change_password/', change_password, name='change_password'),
    path('auth/change-password/', auth_views.PasswordChangeView.as_view(), name='change-password'),

    path('auth/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='verify_refresh'),

    path('create_user_settings/', create_user_settings, name='create_user_settings'),
    path('get_user_settings/', get_user_settings, name='get_user_settings'),
    path('update_user_settings/', update_user_settings, name='update_user_settings'),

    path('recalculation/', recalculate_assets_view, name='recalculate_assets'),
    # path('recalculation/', AssetRecalculator, name='recalculate_assets'),

    path('send_email/', send_email, name='send_email'),

    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

