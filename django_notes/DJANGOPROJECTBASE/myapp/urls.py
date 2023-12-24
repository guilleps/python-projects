from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hello/<str:username>/<int:id>', views.hello, name="hello"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    # path('tasks/<int:id>', views.tasks),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project")
]