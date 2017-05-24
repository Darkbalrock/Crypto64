from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^encrypt+$', views.load_image, name='encryp'),
        url(r'^getFile+$', views.get_file),
    ]