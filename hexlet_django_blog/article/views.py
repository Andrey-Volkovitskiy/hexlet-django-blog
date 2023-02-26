from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article
# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


# class Index(View):
#     def get(self, request, *args, **kwargs):
#         if (kwargs.get('tags') is None and
#                 kwargs.get('article_id') is None):
#             kwargs['tags'] = "python"
#             kwargs['article_id'] = 42

#         return render(request, 'article/index.html', context=kwargs)

# def index(request):
#     return render(request, 'article/index.html', context={
#         'who': __name__})
