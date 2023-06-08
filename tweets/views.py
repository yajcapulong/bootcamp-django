from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView
from .forms import TweetModelForm


# Create your views here.
class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/list_view.html'


class TweetDetailView(DetailView):
    template_name = 'tweets/detail_view.html'

    def get_object(self, query_set=Tweet.objects.all()):
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(id=pk)


class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)
