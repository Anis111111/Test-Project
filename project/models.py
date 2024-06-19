from django.db import models
from django.contrib.auth.models import User
from professor.models import Professor 
from django.core.exceptions import ValidationError

import importlib

def get_student_model():
    students_models = importlib.import_module('students.models')
    return students_models.Student


class Project(models.Model):

    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('backlog', 'Backlog'),
    )
    TYPE_CHOICES = (
        ('web', 'Web'),
        ('desktop', 'Desktop Program'),
        ('ai', 'AI Program'),
        ('full_stack', 'Full Stack App'),
        ('mobile', 'Mobile App'),
    )

    # add project type
    project_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='web', verbose_name='project type')

    # add status for project
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='backlog', verbose_name='status')

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

