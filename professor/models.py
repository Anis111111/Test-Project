from django.db import models
from accounts.models import Profile
# from django.contrib.auth.models import User

# Create your models here.

class Professor(models.Model):
    SPECIALIZATIONS = (
        ('networks', 'networks'),
        ('software', 'software'),
    )

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    phd_certificate = models.FileField(upload_to='certificates/')
    phd_date = models.DateField()
    # personal_number = models.CharField(max_length=20, unique=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATIONS, default='software', verbose_name='specialization')

    def __str__(self):
        return self.user.username
