from django.db import models
from django.contrib.auth.models import User

class StudentGroup(models.Model):
    # تعريفات الحقول لنموذج StudentGroup
    students = models.ManyToManyField('Student', related_name='groups')
    project_idea = models.OneToOneField('project.Project', on_delete=models.CASCADE)

    def __str__(self):
        return f"Group {self.id}"

class Student(models.Model):
    SPECIALIZATIONS = (
        ('networks', 'networks'),
        ('software', 'software'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university_id = models.CharField(max_length=20, unique=True)
    personal_email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', max_length=1 * 1024 * 1024)
    group = models.OneToOneField(StudentGroup, on_delete=models.CASCADE, related_name='student')
    specialization = models.CharField(max_length=50, choices=SPECIALIZATIONS, default='software', verbose_name='specialization')

    def __str__(self):
        return self.user.username
