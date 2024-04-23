from . import views
from django.urls import path

urlpatterns = [
    path("", views.main, name="main"),
    path("testing/", views.testing, name="testing")
]
