from django.conf.urls import url
from administrator import views

urlpatterns=[
    url(r'^index/',views.index,name='index')
]