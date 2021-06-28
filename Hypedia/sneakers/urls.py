from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_sneakers, name="index_sneakers")
]