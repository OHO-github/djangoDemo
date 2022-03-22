from django.urls import path, include
from bookstore import views

urlpatterns = [
    path('', views.index_view),
    path('index', views.index_view),
]