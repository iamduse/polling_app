from django.urls import path
from . import views

urlpatterns = [
    path("", views.hero, name="hero"),        # Landing page at root
    path("login/", views.home, name="home"),  # Login page
    path("logout/", views.user_logout, name="logout"),
    path("vote/", views.vote, name="vote"),
]
