from django.shortcuts import render
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html', context={
            'who': __name__,
        })

# def index(request):
#     return render(request, 'article/index.html', context={
#         'who': __name__})
