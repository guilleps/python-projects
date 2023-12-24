from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>/<int:id>', views.hello),
    path('about/', views.about),
    path('projects/', views.projects),
    # path('tasks/<int:id>', views.tasks),
    path('tasks/', views.tasks),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project)
]