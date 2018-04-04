from django.conf.urls import url
from django.contrib.auth.views import login

from .views import ckeForm
from .views import sucessLogin



urlpatterns = [
    url(r'^login/$',login,name='login'),
    url(r'^sucessLogin/',sucessLogin,name='sucessLogin'),
    url(r'^ckeditorForm/',ckeForm,name='ckeditorForm'),
]
