from django.urls import path

from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="articles_list"),
    path('create/',
         views.ArticleFormCreateView.as_view(),
         name="article_create"),
    path('<int:id>/edit',
         views.ArticleFormEditView.as_view(),
         name="article_update"),
    path('<int:id>/delete',
         views.ArticleDeleteView.as_view(),
         name="article_delete"),
    path('<int:id>/', views.ArticleView.as_view(), name="article"),
    # path('', views.Index.as_view(), name='article'),
    # path(
    #     '<str:tags>/<int:article_id>/',
    #     views.Index.as_view(), name='article_tag_id'),
]
