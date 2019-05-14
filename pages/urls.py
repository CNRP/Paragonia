from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^article/(?P<id>\d+)/$', views.article, name='article'),
]
