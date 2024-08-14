from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from articles.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
from articles.apps import ArticlesConfig

app_name = ArticlesConfig.name


class ArticleEditView:
    pass


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('view/<int:pk>', ArticleDetailView.as_view(), name='view'),
    path('edit/<int:pk>', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
