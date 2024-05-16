from django.urls import path, include
from . import views

app_name="portfolioapp"

urlpatterns = [
    path("", views.homepage, name="home")
]