from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students_page, name='students_page'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
