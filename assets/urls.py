# from django.db import models
# from django.contrib.auth.models import User
from django.urls import path, include

from assets import views

urlpatterns = [
    # path('ping/', views.ping, name='ping'),
    path('api/', include('assets.api.urls')),
]
