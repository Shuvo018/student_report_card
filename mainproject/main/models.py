from django.db import models

class modelsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.department
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.CharField(unique=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    is_deleted = models.BooleanField(default=False)

    objects = modelsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "Student"

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name='studentmark', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='subjectmark', on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.student_name} - {self.subject.subject_name}"
    
    class Meta:
        unique_together = ('student', 'subject')

