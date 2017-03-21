from django.conf.urls import url
from student import views

app_name = 'student'
urlpatterns=[
    url(r'^index/$',views.index,name='index')
]