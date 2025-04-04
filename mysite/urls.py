"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home_view
from resume.views import resume_view
from interests.views import interests_view
from contact.views import contact_view
from gallery.views import gallery_view
from poetry.views import poetry_view
from django.http import HttpResponseNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('resume/', resume_view, name='resume'),
    path('interests/', interests_view, name='interests'),
    path('contact/', contact_view, name='contact'),
    path('gallery/', gallery_view, name='gallery'),
    path('poetry/', poetry_view, name='poetry'),
]
urlpatterns += [
    path("favicon.ico", lambda request: HttpResponseNotFound()),
]
