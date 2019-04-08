from django.urls import path
from . import views


urlpatterns = [
    path('newsletter_singup/',views.newsletter_singup,name='newsletter_singup'),
    path('newsletter_unsubscribe/',views.newsletter_unsubscribe,name='newsletter_unsubscribe'),
    path('control_newsletter/',views.control_newsletter,name='control_newsletter'), 
]