from django.urls import path
from . import viewsw

urlpatterns = [
    path('', resume_view, name='resume'),
    path('home/', resume_view, name='resume'),
    path('gallery/', gallery_view, name='gallery'),
    path('contact/', contact_view, name='contact'),
    path('poetry/', poetry_view, name='poetry'),
]
