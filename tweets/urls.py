from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('',  TweetListView.as_view(), name='list_view'),
    re_path(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail_view'),
    path('create/', TweetCreateView.as_view(), name='create_view'),
]