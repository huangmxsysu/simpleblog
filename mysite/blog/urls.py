from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/new2/$', views.post_new, name='post_new2'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='post_edit'),
]