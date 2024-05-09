from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:category_name>/', views.home, name="filter_by_category"),
    path('single-post/<str:pk>/', views.single_post, name="single-post"),
    path('search/', views.search, name="search"),
]

