from django.urls import path, include

urlpatterns = [
    path('', include('app_shop.routers.shop_router')),
]
