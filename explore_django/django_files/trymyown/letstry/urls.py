from django.urls import path

from .views import homePageView
from .views import trypageview
from .views import aboutus

urlpatterns=[
    path("", homePageView, name="home"),
    path("tryindex.html",trypageview),
    path("about-us.html",aboutus),
]
