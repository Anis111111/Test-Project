from django.db import models
from django.contrib.auth.models import User
from professor.models import Professor 
import importlib

def get_student_model():
    students_models = importlib.import_module('students.models')
    return students_models.Student

# Create your models here.

class ProjectStatus(models.TextChoices):
    DONE = "Done"
    IN_PROCESSING = "In_Processing"
    BACK_IN_THE_LOG = "Back_In_The_Log"

class Category(models.TextChoices):
    WEBS = 'Webs'
    PROGRAMS = 'Program'
    APPS = 'Apps'
    AI = 'AI'
    FULL_STACK = 'Full_stack'

# class Project(models.Model):
#     id = models.IntegerField(default = 0, primary_key=True)

#     # doctor = models.ForeignKey(Doctor , null=True , on_delete = models.PROTECT)
#     # user = models.ForeignKey(User , null=True , on_delete=models.PROTECT)

#     title = models.CharField(max_length = 200 , default = "" ,blank = False)
#     project_status = models.CharField(max_length = 30 ,default = "" ,blank = False , choices=ProjectStatus)
#     descripthion = models.TextField(max_length = 1000 , default = "" ,blank = False)

#     category = models.CharField(max_length = 50 , default = "" ,blank = False , choices=Category)
#     ratings  = models.DecimalField(max_digits=5 , default=0 , decimal_places=1 )

#     createAt = models.DateTimeField(auto_now_add = True)

#     def __str__(self):
#         return self.title

from django.core.exceptions import ValidationError

class Project(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    idea = models.TextField(unique=True)

    professor = models.ForeignKey(Professor, related_name='projects', on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(get_student_model(), related_name='projects')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_students(self):
        return get_student_model().objects.filter(project=self)
    
    def __str__(self):
        return self.title
        
    # Check only if the model already exists.
    def save(self, *args, **kwargs):
        if self.pk:
            student_count = self.students.count()
            if student_count < 4 or student_count > 6:
                raise ValidationError('The number of students must be between 4 and 6.')
        super(Project, self).save(*args, **kwargs)

    # Ensure the basic validation is executed.
    def clean(self):
        super(Project, self).clean() 
        student_count = self.students.count()
        if student_count < 4 or student_count > 6:
            raise ValidationError('The number of students must be between 4 and 6.')


class Review(models.Model):
    project = models.ForeignKey(Project , null = True , on_delete = models.CASCADE , related_name = 'reviews')

    # user = models.ForeignKey(User , null = True , on_delete = models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    comment = models.TextField(max_length = 1000 , default = "" , blank = False)
    createAt = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.comment

