from django.conf.urls import url
from django.contrib import admin

from app.views import IndexView, SongView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^(?P<song_url>.*)', SongView.as_view(), name='song_view'),# USE THIS URL PATTERN AT THE VERY BOTTOM!!!
]
