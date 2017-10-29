from django.conf.urls import url
from basic_app import views
from django.contrib.auth import views as auth_views

app_name='basic_app'

urlpatterns=[
    url(r'^register/$',views.register, name='register'),
    url(r'^user_login/$',auth_views.login,{'template_name':'login.html',}, name='user_login'),
    url(r'^profile/$', views.profile, name='profile'),
]