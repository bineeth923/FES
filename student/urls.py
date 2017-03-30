from django.conf.urls import url
from student import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^form/([0-9]+)',views.forms , name='form')
]