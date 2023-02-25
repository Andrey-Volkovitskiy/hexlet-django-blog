from django.shortcuts import render
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        if (kwargs.get('tags') is None and
                kwargs.get('article_id') is None):
            kwargs['tags'] = "python"
            kwargs['article_id'] = 42

        return render(request, 'article/index.html', context=kwargs)

# def index(request):
#     return render(request, 'article/index.html', context={
#         'who': __name__})
