from django.urls import path

from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="articles_list"),
    # path('', views.Index.as_view(), name='article'),
    # path(
    #     '<str:tags>/<int:article_id>/',
    #     views.Index.as_view(), name='article_tag_id'),
]
