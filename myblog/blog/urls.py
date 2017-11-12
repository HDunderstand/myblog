from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^post/(?P<pk>[0-9]+)/$', views.single, name='single'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
