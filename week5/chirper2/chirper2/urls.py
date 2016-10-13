"""chirper2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app.views import index_view, about_view, ChirpView, ChirpDetailView, \
                      ChirpCreateView, ChirpUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', index_view, name="index_view"),
    url(r'^chirps/$', ChirpView.as_view(), name="chirp_view"),
    url(r'^chirps/create/$', ChirpCreateView.as_view(), name="chirp_create_view"),
    url(r'^chirps/(?P<pk>\d+)/$', ChirpDetailView.as_view(), name="chirp_detail_view"),
    url(r'^chirps/(?P<pk>\d+)/update/$', ChirpUpdateView.as_view(), name="chirp_update_view"),
    url(r'^about/$', about_view, name="about_view")
]
