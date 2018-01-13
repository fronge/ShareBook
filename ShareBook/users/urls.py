from django.conf.urls import url,include
from django.contrib import admin
import users.views

urlpatterns = [
    url(r'^$', users.views.index),
]