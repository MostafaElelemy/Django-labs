from django.shortcuts import render, redirect


students = [
    {"id": 1, "name": "Ali", "age": 18, "grade": "A"},
    {"id": 2, "name": "Sara", "age": 19, "grade": "B"},
    {"id": 3, "name": "Ahmed", "age": 20, "grade": "C"},
    {"id": 4, "name": "Mona", "age": 21, "grade": "B+"},
    {"id": 5, "name": "Omar", "age": 22, "grade": "A+"},
]

def home(request):
    return render(request, 'home.html')

def students_page(request):
    return render(request, 'students.html', {'students': students})

def delete_student(request, student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return redirect('students_page')
