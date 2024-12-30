from django.views import View
from django.shortcuts import render, get_object_or_404

from app_blog.models import Article, ArticleReview

class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.filter(published=True).order_by('-updated')
        return render(request, 'app_blog/article/article_list.html', {
            'articles': articles,
        })
    

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id, published=True)
        article_reviews = ArticleReview.objects.filter(article=article_id, status=ArticleReview.STATUS_APPROVED).order_by('-created')

        return render(request, 'module_blog/article/article-view.html', {
            'article': article,
            'articleReviews': article_reviews,
        })
