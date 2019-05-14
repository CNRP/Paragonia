from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^pages/', include('pages.urls')),
    url(r'^$', views.index, name='index'),
    url('guides/', views.guides, name='guides'),
    url('news/',  include('pages.urls')),
]