from django.urls import path, include

urlpatterns = [
    path('blog/', include('app_blog.routers.blog_router')),
]
