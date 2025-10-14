from django.shortcuts import render

# Create your views here.
def student_list(request,name):
    return render(request, 'index.html', {'name': name})
