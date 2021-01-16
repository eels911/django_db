
from django.urls import path
from . import views
# from .views import VisitsView


app_name = "visits"

urlpatterns = [
    path('', views.index),
    path('visits', views.VisitsView.as_view())
]