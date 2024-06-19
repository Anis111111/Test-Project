from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save ,pre_save
from django.core.validators import RegexValidator

# Create your models here.

# class PaymentMode(models.TextChoices):
#     COD = "COD"
#     CARD = "CARD"

class Profile(models.Model):
    user = models.OneToOneField(User , related_name = 'profile' , on_delete = models.CASCADE)
    
    reset_password_token = models.CharField(max_length = 50 , default = "" , null = True ,blank = True)
    reset_password_expire = models.DateTimeField(null = True , blank = True)
    
    id = models.IntegerField(default = 0 , primary_key=True ,auto_created=True)
    
    img = models.ImageField(upload_to = 'photos/' , height_field='height', width_field='width' , null=True , blank=True) # user_upload_to
    height = models.PositiveIntegerField(default=5)
    width = models.PositiveIntegerField(default=5)

    phone = models.CharField(max_length = 10 , null = True, unique=True,
    validators=[
        RegexValidator(
            regex=r'^\d{10}$',
            message='The phone must be 10 numbers long.',
            code='invalid_phone'
        ),
    ] )

    # email = models.EmailField(max_length=75, null = False,blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add = True)
    
    # def user_upload_to(instance, filename):
    #     return f'users/{instance.user.username}/{filename}'

    def __str__(self):
        return self.name


@receiver(pre_save , sender = User)
def save_profile(sender , instance , created , **kwargs):

    print('instance',instance)
    user =  instance

    if created:
        profile = Profile(user = user)
        profile.save()


