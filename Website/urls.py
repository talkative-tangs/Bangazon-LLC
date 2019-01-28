from django.urls import path
from . import views

app_name = 'Website'
urlpatterns = [
  path('', views.index, name='index'),
  path('employees/', views.employees, name='employees'),
  path('departments/', views.departments, name='departments'),
  path('computers/', views.computers, name='computers'),
  path('training/', views.training, name='training'),
]