from django.urls import path
from . import viewsw

urlpatterns = [
    path('', home_view, name='home'),
]
