from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^singup/$', views.singup, name='singup'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
