from django.urls import path

from app_blog.views import article_view

urlpatterns = [
    path('', article_view.ArticleListView.as_view(), name='articleList'),
    path('<int:id>/', article_view.ArticleView.as_view(), name='articleViewShortLink'),
    path('<int:id>/<str:slug>/', article_view.ArticleView.as_view(), name='articleViewFullLink'),
]