from django.urls import path

from . import views
app_name = 'contactForm'
urlpatterns = [
    path('contact/', views.emailView, name='contact'),
    path('success/', views.successView, name='success'),
]