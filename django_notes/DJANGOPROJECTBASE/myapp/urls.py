from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>/<int:id>', views.hello),
    path('about/', views.about)
]