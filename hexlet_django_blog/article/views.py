from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View

from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article saved.')
            return redirect('articles_list')

        return render(request, 'article/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        article = Article.objects.get(id=id)
        form = ArticleForm(instance=article)
        return render(request, 'article/edit.html', {
            'form': form,
            'id': id})

    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        article = Article.objects.get(id=id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article saved.')
            return redirect('articles_list')

        return render(request, 'article/edit.html', {
            'form': form,
            'id': id})
