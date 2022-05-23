from django.urls import  path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Bharath", views.Bharath, name="Bharath"),
    path("<str:name>", views.greet, name="greet")
]