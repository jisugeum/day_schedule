from django.conf.urls import url
from . import views

app_name = 'calender'
urlpatterns = [
    url(r'^index/$', views.index, name ='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^calendar/event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]