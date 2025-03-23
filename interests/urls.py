from django.urls import path
from . import viewsw

urlpatterns = [
    path('', home_view, name='interests'),
    path('poetry/', poetry_view, name='poetry'),
    path('gallery/', gallery_view, name='gallery'),
    path('contact/', contact_view, name='contact'),
    path('resume/', resume_view, name='resume'),
]
