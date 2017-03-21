from django.conf.urls import url
from teacher import views

urlpatterns=[
    url(r'^index/',views.index,name='index')
]