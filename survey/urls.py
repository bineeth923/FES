from django.conf.urls import url, include
from  administrator import views as admin_view
from survey import views as survey_view

urlpatterns=[
    url(r'^student/', include('student.urls', namespace='student')),
    url(r'^teacher/', include('teacher.urls', namespace='teacher')),
    url(r'^administrator/', include('administrator.urls', namespace='administrator')),
    url(r'^$', survey_view.common_login , name='login'),
]