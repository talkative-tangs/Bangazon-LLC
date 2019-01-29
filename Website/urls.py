from django.urls import path
from . import views

app_name = 'Website'
urlpatterns = [
  path('', views.index, name='index'),
  path('employees/', views.employees, name='employees'),
  path('departments/', views.departments, name='departments'),
  path('departments/add', views.departments_add, name='departments_add'),
  path('computers/', views.computers, name='computers'),
  path('computer/<int:computer_id>/', views.computer, name='computer'),
  path('new_computer/', views.new_computer, name='new_computer'),
  path('training/', views.training, name='training'),
  path('training/add', views.add_training_form, name='add_training_form'),
  path('training/post', views.post_training, name='post_training'),
]