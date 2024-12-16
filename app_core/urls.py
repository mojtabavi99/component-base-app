from django.urls import path, include

urlpatterns = [
    path('', include('app_core.routers.site_router')),
]
