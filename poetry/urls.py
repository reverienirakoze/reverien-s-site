from django.urls import path
from . import viewsw

urlpatterns = [
    path('', poetry_view, name='poetry'),
    path('home/'), home_view, name='home',
    path('interests/'), interests_view, name='interests',
    path('gallery/'), gallery_view, name='interests',
    path('contact/'), contact_view, name='contact',
    path('resume/)', resume_view, name='resume',
]
