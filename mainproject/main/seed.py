from faker import Faker
import random
from .models import Department, Student, Subject, SubjectMarks, ReportCard
from django.db.models import Sum
def generate_fake_student_details(n=100) -> None:
    fake = Faker()
    for _ in range(n):
            try:
                departments_objs = Department.objects.all()
                random_index = random.randint(0, len(departments_objs)-1)
                department = departments_objs[random_index]
                student_id = f'STU-0{random.randint(100, 999)}'
                student_name = fake.name()
                student_email = fake.email()
                student_age = random.randint(18, 30)
                student_address = fake.address()

                Student.objects.create(
                    department=department,
                    student_id=student_id,
                    student_name=student_name,
                    student_email=student_email,
                    student_age=student_age,
                    student_address=student_address
                )
            except Exception as e:
                print(f"Error seeding database: {e}")
    
        
def create_student_marks() -> None:
    try:
        student = Student.objects.all()
        subject = Subject.objects.all()
        for stu_obj in student:
            for sub_obj in subject:
                marks = random.randint(0, 100)
                SubjectMarks.objects.create(student=stu_obj, subject=sub_obj, marks=marks)
        print("Student marks created successfully.")
    except Exception as e:
        print(f"Error creating student marks: {e}")

def generate_report_card() -> None:
    try:
        ranks = Student.objects.annotate(marks = Sum('studentmark__marks')).order_by('-marks')

        i = 1
        for rank in ranks:
            ReportCard.objects.create(student=rank, student_rank=i)
            i += 1

    except Exception as e:
        print(f"Error generating report card: {e}")


        
    