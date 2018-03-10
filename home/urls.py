#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Home app url configuration."""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),

    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    # path("signin/", views.signin, name="signin"),
    # path("logout/", views.logout, name="logout"),

]
