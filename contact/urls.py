from django.urls import path
from . import viewsw

urlpatterns = [
    path('', contact_view, name='contact'),
    path('home/', home_view, name='home'),
    path('gallery/', gallery_view, name='gallery'),
    path('poetry/', poetry_view, name='poetry'),
    path('resume/', resume_view, name='resume'),
]
