from django.urls import path
from courses.views import course_list, delete_course


urlpatterns = [
    path('courses/', course_list,name="courses"),
    path('delete/', delete_course,name="delete_course"),
    
]

