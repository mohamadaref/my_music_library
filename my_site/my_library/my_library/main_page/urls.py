from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
from main_page import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^(?P<musician_name>[a-zA-Z_+ ]+)/(?P<alb_name>[a-zA-Z_+]+)/(?P<song_name>[a-zA-Z_+]+)/$', views.downloadmu, name='musician\'s name + album\'s name + song\'s name'),
    url(r'^(?P<alb_name>[a-zA-Z_+ 0-9]+)/(?P<song_name>[a-zA-Z_+]+)/$', views.downloadal, name='album\'s name + song\'s name'),
    re_path(r'^(?P<song_name>[a-zA-Z_+]+)/$', views.download, name='song\'s name'),
    re_path(r'^(?P<alb_name>[a-zA-Z_+ 0-9]+)/$', views.alb_detail, name='alb_det'),
    re_path(r'^(?P<musician_name>[a-zA-Z_+ 0-9]+)/$', views.musician_detail, name='musician_det'),
]
