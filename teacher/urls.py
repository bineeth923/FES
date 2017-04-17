from django.conf.urls import url
from teacher import views

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^index/([0-9]+)/$' , views.forms , name='all_forms'),
    url(r'index/([0-9]+)/([0-9]+)/$', views.result, name='result' )

]