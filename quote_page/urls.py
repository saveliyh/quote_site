from django.urls import path
from . import views


urlpatterns = [
    path("", views.random_quote, name="index"),
    path("statistics", views.statistics, name="statistics"),
    path("add_quote", views.add_quote, name="add_quote"),
    path("success_add", views.add_quote, name="success_add"),
    path("fail_add", views.add_quote, name="fail_add"),
]
