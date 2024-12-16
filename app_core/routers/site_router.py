from django.urls import path

from app_core.views import site_view

urlpatterns = [
    path('', site_view.HomeView.as_view(), name='home'),
]