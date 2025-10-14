from django.urls import path
from student.views import student_list
urlpatterns = [
     path('student/<str:name>', student_list),
]