from django.urls import path, include


urlpatterns = [
    path('api/', include('assets.api.urls')),
]
