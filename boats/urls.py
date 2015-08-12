from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boats/(?P<boat_url>[^/]+)/$', views.boat, name='boat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
