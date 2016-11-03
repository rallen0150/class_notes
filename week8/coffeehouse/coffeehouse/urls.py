from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from menu.views import SpecialListView, SpecialCreateView, SpecialUpdateView, SpecialListAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SpecialListView.as_view(), name='special_list_view'),
    url(r'^create/$', SpecialCreateView.as_view(), name='special_create_view'),
    url(r'^update/(?P<pk>\d+)/$', SpecialUpdateView.as_view(), name='special_update_view'),
    url(r'^api/specials/$', SpecialListAPIView.as_view, name='special_list_api_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
