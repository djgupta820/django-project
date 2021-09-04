from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('html/', views.html, name="html"),
    path('css/', views.css, name="css"),
    path('javascript/', views.javascript, name="js"),
    path('php/', views.php_, name="php_"),
    path('c/', views.c, name="c"),
    path('cpp/', views.cpp, name="cpp"),
    path('java/', views.java, name="java"),
    path('python/', views.py,name="python"),
    path('linux/', views.linux, name="linux"),
    path('projects/', views.projects, name="projects"),
]