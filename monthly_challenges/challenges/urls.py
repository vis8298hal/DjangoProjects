from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("Error", views.show_error, name="show_error"),
    path("<int:month>", views.monthly_challenge_by_number, name="monthly_challenge_by_number"),
    path("<str:month>", views.monthly_challenge, name="monthly_challenge"),
]