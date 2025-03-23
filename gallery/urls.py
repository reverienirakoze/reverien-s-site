from django.urls import path
from . import viewsw

urlpatterns = [
    path('', gallery_view, name='gallery'),
    path('home/', home_view, name='home'),
    path('interests/', interests_view, name='interests'),
    path('resume/', resume_view, name='interests'),
    path('poetry/', poetry_view, name='poetry'),
]
