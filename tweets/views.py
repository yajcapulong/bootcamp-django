from django.shortcuts import render, redirect
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from django.forms.utils import ErrorList
from django import forms
from .mixins import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.-
class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/list_view.html'

class TweetDetailView(DetailView):
    template_name = 'tweets/detail_view.html'

    def get_object(self, query_set=Tweet.objects.all()):
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(id=pk)

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = reverse_lazy('tweets:list_view')
    login_url = '/admin/'

 # class TweetUpdateView
class TweetUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    success_url = '/tweet/'
    template_name = 'tweets/update_view.html'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = '/tweet/'
    template_name = 'tweets/delete_confirm.html'
    login_url = '/admin/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
