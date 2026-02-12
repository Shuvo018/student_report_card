from django.shortcuts import render, redirect
from .models import Subject, Student, Department, SubjectMarks
from django.core.paginator import Paginator

# Create your views here.
def show_student_list(request):
    query = Student.objects.all()
    
    paginator = Paginator(query, 15)  # Show 15 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'student_list.html', context={'query':page_obj,'page_title': "Student list"})
def add_student(request):
    if request.method == "POST":
        data = request.POST
        try:
            department_instance = Department.objects.get(
                department=data['department']
            )
            
            print(department_instance)
            Student.objects.create(
                department = department_instance,
                student_id = data['student_id'],
                student_name = data['student_name'],
                student_email = data['student_email'],
                student_age = data['student_age'],
                student_address = data['student_address'],
            )
            print("student added successfully")
        except Exception as e:
            print(e)
        return redirect("/")
    return render(request, 'add_student.html', context={'page_title': "Add student"})

def deleted_stu_list(request):
    query = Student.admin_objects.filter(is_deleted=True)
    return render(request, "deleted_student.html",  context={'query':query,'page_title': "deleted_stu_list"})

def recover_stu(request, id):
    Student.admin_objects.filter(student_id=id).update(is_deleted=False)
    print('recover successfully')
    return redirect("/deleted_stu_list/")

def delete_per_stu(request, id):
    Student.admin_objects.get(student_id=id).delete()
    print("student delete permanently")
    return redirect("/")

def delete_stu(request, id):
    Student.objects.filter(student_id=id).update(is_deleted=True)
    return redirect("/")

def student_mark(request):
    return render(request, 'student_mark.html')

def department(request):
    if request.method == "POST":
        data = request.POST
        if data['department'] is not None:
            try:
                Department.objects.create(department=data['department'])
                print("department added successfully")
            except Exception as e:
                print("This department exist")
            return redirect("/department/")
    query = Department.objects.all()
    return render(request, 'department.html', context={'query':query,'page_title': "Department"})

def subject(request):
    if request.method == "POST":
        data = request.POST
        if data['subject'] is not None:
            try:
                Subject.objects.create(subject_name=data['subject'])
                print("subjected added successfully")
            except Exception as e:
                print("This subject exist")
            return redirect("/subject/")
    query = Subject.objects.all()
        
    paginator = Paginator(query, 5)  # Show 15 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'subject.html', context={'query':page_obj,'page_title': "Subject"})