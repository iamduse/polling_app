from django.conf.urls.static import static
from django.urls import path

from poll_site import settings
from . import views

urlpatterns = [
    path("", views.hero, name="hero"),        # Landing page at root
    path("login/", views.home, name="home"),  # Login page
    path("logout/", views.user_logout, name="logout"),
    path("vote/", views.vote, name="vote"),
]

# This code check the image root
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)