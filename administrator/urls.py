from django.conf.urls import url, include
from administrator import views as admin_view

urlpatterns=[
    url(r'^index/$',admin_view.index,name='index'),
    url(r'^logout/$' , admin_view.logout_user , name='logout'),
    url(r'^add_subject/$' , admin_view.add_subject , name="add_subject"),
    url(r'^add_semester/$', admin_view.add_semester , name='add_semester'),
    url(r'^add_teacher/$' , admin_view.add_teacher , name='add_teacher'),
    url(r'^survey/$', admin_view.survey_creation, name='survey'),
    url(r'^add_question/$', admin_view.add_question, name='add_question'),
]