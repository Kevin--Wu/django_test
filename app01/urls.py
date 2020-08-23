from django.conf.urls import url

import app01.views as views

urlpatterns = [ 
    # urls(r'^login/(?P<m>[0-9]{2})/$', views.index),
    url(r'^hello$', views.hello),
    url(r'^testparam/(?P<testnum>[0-9]+)/(?P<testalpha>[a-z]+)', views.testparam),
] 