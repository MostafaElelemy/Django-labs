from django.shortcuts import render

# Create your views here.

def course_list(request,name):
    return render(request, 'cou.html', {'name': name})
