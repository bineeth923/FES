from django.conf.urls import url
from student import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^sem/([0-9]+)',views.allFroms , name='form'),
    url(r'^sem/form/([0-9]+)',views.formFill , name='fillForm'),
]