#__author__ = 'min'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/',views.detail,name='detail'),
    url(r'^vote/',views.vote,name='vote'),
    url(r'^$',views.index,name='index'),
    url(r'^pytest/',views.pytest,name='pytest'),

]
