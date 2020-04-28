from django.conf.urls import url
from django.urls import re_path, path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]