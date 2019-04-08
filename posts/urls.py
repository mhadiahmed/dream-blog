from django.urls import path,re_path
from . import views


app_name='Post'
urlpatterns = [
	
    path('',views.list,name='index'),
    # path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    re_path(r'^(?P<id>\d+)/detail/$',views.detail,name='detail-page'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',views.list,name='category'),
    
    # re_path(r'^category/$',views.category,name='category-page')
]



