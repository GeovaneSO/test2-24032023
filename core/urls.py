from django.urls import path
from . import views

urlpatterns = [
    path("", views.view1, name="register"),
    path("upload/", views.upload, name="upload"),
    path("upload/", views.upload, name="upload"),

]