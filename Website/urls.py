from django.urls import path
from . import views

app_name = 'Website'
urlpatterns = [
  path('', views.index, name='index'),
  path('employees/', views.employees, name='employees'),
  path('employees/add/', views.employees_add, name='employees_add'),
  path('departments/', views.departments, name='departments'),
  path('departments/add', views.departments_add, name='departments_add'),
  path('computers/', views.computers, name='computers'),
  path('computers/detail/<int:computer_id>/', views.computers_detail, name='computers_detail'),
  path('computers/add/', views.computers_add, name='computers_add'),
  path('training/', views.training, name='training'),
  path('training/add', views.training_add, name='training_add'),
]