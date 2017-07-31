from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^json/$', views.var_json, name='var_json')
]