from django.shortcuts import render, redirect

# Create your views here.
students = [
    {'id': 1, 'name': 'Ali', 'grade': 'A'},
    {'id': 2, 'name': 'Sara', 'grade': 'B'},
    {'id': 3, 'name': 'Omar', 'grade': 'C'},
]


def course_list(request):
    return render(request, 'base.html')

def delete_student(request):
    return render(request, 'data.html')






