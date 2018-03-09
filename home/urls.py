#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Home app url configuration."""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login, name="login"),
    path("about/", views.about, name="about"),
]
