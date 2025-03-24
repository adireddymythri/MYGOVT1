# users/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('submit_problem/', views.submit_problem, name='submit_problem'),
    path('view_problems/', views.user_dashboard, name='view_problems'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
]
