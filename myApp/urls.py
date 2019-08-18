from django.conf.urls import url
from .views import Main, Create_User, Create_Connection, saveProfile, friendSearch

urlpatterns = [
    url(r'^main/$', Main.as_view(), name='main'),
    url(r'^create_user/$', Create_User.as_view(), name='create_user'),
    url(r'^create_connection/$', Create_Connection.as_view(), name='create_connection'),

    url(r'^saveProfile/(?P<id>\d+)/$', saveProfile.as_view(), name='saveProfile'),

    url(r'^friendSearch/$', friendSearch, name='friendSearch'),
]

