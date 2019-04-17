from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.index, name='home'),
    path('movies/view/<int:id>/', views.view_movie, name='view_movie'),
    path('movies/update/<int:id>/', views.update_movie, name='update_movie'),
    path('movies/delete/<int:id>/', views.delete_movie, name='delete_movie'),
    path('actors/view/<int:id>/', views.view_actor, name='view_actor'),
    path('actors/update/<int:id>/', views.update_actor, name='update_actor'),
    path('actors/delete/<int:id>/', views.delete_actor, name='delete_actor'),
    path('comments/update/<int:id>/', views.update_comment, name='update_comment'),
    path('comments/delete/<int:id>/', views.delete_comment, name='delete_comment'),
    path('actors/', views.view_actors, name='actors'),
    path('awards/', views.view_awards, name='awards'),
]