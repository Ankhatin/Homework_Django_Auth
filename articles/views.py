from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from articles.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body',)
    success_url = reverse_lazy('articles:article_list')

    def form_valid(self, form):
        if form.is_valid():
            article = form.save()
            article.slug = slugify(article.title)
            article.save()
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        self.queryset = super().get_queryset(*args, **kwargs)
        self.queryset = self.queryset.filter(is_published=True)
        return self.queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_review += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)

    def form_valid(self, form):
        if form.is_valid():
            article = form.save()
            article.slug = slugify(article.title)
            article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles:view', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:article_list')