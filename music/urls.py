from django.urls import path, include
from music import views

urlpatterns = [
    path('', views.index_view),
    path('index', views.index_view),
]
