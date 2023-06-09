from django.urls import path, re_path
from .views import *
app_label = 'tweets'

urlpatterns = [
    path('',  TweetListView.as_view(), name='list_view'),
    path('create/', TweetCreateView.as_view(), name='create_view'),
    re_path(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail_view'),
    re_path(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update_view'),
    re_path(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete_view'),
]