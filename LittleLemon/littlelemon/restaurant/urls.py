# define URL route for index() view
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_view, name='home'),
]
