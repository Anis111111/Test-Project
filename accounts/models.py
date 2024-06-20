from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save ,pre_save
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.

# class PaymentMode(models.TextChoices):
#     COD = "COD"
#     CARD = "CARD"


class Profile(models.Model):
    user = models.OneToOneField(User , related_name = 'profile' , on_delete = models.CASCADE)
    
    # reset_password_token = models.CharField(max_length = 50 , default = "" , null = True ,blank = True)
    # reset_password_expire = models.DateTimeField(null = True , blank = True)
    # id = models.IntegerField(default = 0 , primary_key=True ,auto_created=True)
    
    img = models.ImageField(upload_to = 'photos/' , height_field='height', width_field='width' , null=True , blank=True) # user_upload_to
    height = models.PositiveIntegerField(default=5)
    width = models.PositiveIntegerField(default=5)

    phone = models.CharField(max_length = 20 , null = True, unique=True,
    validators=[
        RegexValidator(
            regex=r'^\d{20}$',
            message='The phone must be 20 numbers long.',
            code='invalid_phone'
        ),
    ] )

    # email = models.EmailField(max_length=75, null = False,blank=False, unique=True)
    personal_email = models.EmailField(unique=True)
    age = models.IntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(100)
        ],
        help_text="The age must be between 18 and 100 years."
    )
    date_created = models.DateTimeField(auto_now_add = True)
    
    # def user_upload_to(instance, filename):
    #     return f'users/{instance.user.username}/{filename}'

    def __str__(self):
        return self.name


@receiver(post_save, sender=Profile)
def save_profile(sender, instance, created, **kwargs):
    
    print('instance',instance)
    user =  instance

    if created:
        profile = Profile(user = user)
        profile.save()
    else:
        pass


