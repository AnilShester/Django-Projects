from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^login$', views.user_login, name='login')
]