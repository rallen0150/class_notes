
from django.conf.urls import url
from django.contrib import admin

from menu_api.views import SpecialListCreateAPIView, SpecialDetailUpdateDestroyAPIView, IngredientListCreateAPIView, \
                           IngredientDetailUpdateDestroyAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ingredients/$', IngredientListCreateAPIView.as_view(), name='ingredient_list_create_api_view'),
    url(r'^ingredients/(?P<pk>\d+)/$', IngredientDetailUpdateDestroyAPIView.as_view(), name='ingredient_detail_destroy_api_view'),
    url(r'^specials/$', SpecialListCreateAPIView.as_view(), name='special_list_create_api_view'),
    url(r'^specials/(?P<pk>\d+)/$', SpecialDetailUpdateDestroyAPIView.as_view(), name='special_detail_destroy_api_view'),
]
