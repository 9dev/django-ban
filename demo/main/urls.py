from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(
        r'^$',
        views.dummy,
        name='dummy',
    ),
    url(
        '^login/',
        auth_views.login,
        {'template_name': 'main/login.html'},
        name='login',
    ),
]
