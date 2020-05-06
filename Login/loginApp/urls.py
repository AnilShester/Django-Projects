from django.conf.urls import url
from loginApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name= 'user_logout'),
    url(r'^users_list/$', views.view_users, name='users_list')
]