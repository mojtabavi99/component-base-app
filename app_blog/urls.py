from django.urls import path, include

urlpatterns = [
    path('', include('app_blog.routers.article_router')),
]
