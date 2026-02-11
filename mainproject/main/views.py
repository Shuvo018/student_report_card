from django.shortcuts import render

# Create your views here.
def show_student_list(request):
    return render(request, 'student_list.html')

def add_student(request):
    return render(request, 'add_student.html')
def student_mark(request):
    return render(request, 'student_mark.html')