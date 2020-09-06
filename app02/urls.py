from django.conf.urls import url

import app02.views as views

urlpatterns = [ 
    # urls(r'^login/(?P<m>[0-9]{2})/$', views.index),
    url(r'^hello$', views.hello),
] 