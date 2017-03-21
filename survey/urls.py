from django.conf.urls import url, include
from survey import views
urlpatterns=[
    url(r'^student/', include('student.urls', namespace='student')),
    url(r'^teacher/', include('teacher.urls', namespace='teacher')),
    url(r'^administrator/', include('administrator.urls', namespace='administrator')),
    url(r'^$', views.common_login , name='login'),

]