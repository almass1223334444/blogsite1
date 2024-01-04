from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.indexpage, name="index"),
    path("home", views.indexpage, name="index"),
    path("home/", views.indexpage, name="index"),
    path("about", views.aboutpage, name="about"),
    path("about/", views.aboutpage, name="about"),
    path("contact", views.contactpage, name="contact"),
    path("contact/", views.contactpage, name="contact"),
    path("post", views.postpage, name="post"),
    path("post/", views.postpage, name="post"),
    path("login", views.loginpage, name="login"),
    path("login/", views.loginpage, name="login"),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)