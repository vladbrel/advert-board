from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
        path('',views.index, name='home'),
        path('about', views.about, name='about'),
        path('create', views.create, name='create'),
        path('list', views.ad_list, name='list'),
        url(r'^(?P<category_slug>[-\w]+)/$', views.ad_list, name='ad_list_by_category'),
        url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ad_detail, name ='ad_detail')
]

