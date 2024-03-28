from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path('create_project/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<project_id>/add_task/', views.add_task, name='add_task'),
    path('project/<int:project_id>/task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('project/<int:project_id>/task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
   
]