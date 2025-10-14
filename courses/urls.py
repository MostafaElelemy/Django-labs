from django.urls import path
from courses.views import course_list

urlpatterns = [
    path('courses/<str:name>', course_list,name="courses"),
]