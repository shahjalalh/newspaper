__author__ = 'shahjalal'
from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.PostDetailView.as_view(),
        name='post-detail'),
]
