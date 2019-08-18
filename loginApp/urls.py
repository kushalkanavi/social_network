from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import Index, Register, CreateUser

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'loginApp/login_user.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'loginApp/logged_out.html'}, name='logout'),

    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^createuser/$', CreateUser.as_view(), name='createuser'),

    url(r'^$', Index.as_view(), name='index'),
]
