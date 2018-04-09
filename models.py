from django.db import models
from django.utils import timezone
import uuid
from django.core.validators import MinLengthValidator, RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .validators import *
from .helpers.models_helper import *
from .helpers.views_helper import *


class Admin(models.Model):
    MailId = models.EmailField(unique = True)
    Password = models.CharField(max_length = 25, validators = [MinLengthValidator(8)])

    def __str__(self):
        return self.MailId
    
    class Meta:
        ordering = ["MailId"]

@receiver(post_save, sender = Admin)
def save_admin(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.MailId, email=instance.MailId, password=instance.Password)
        user.profile.type = 'a'
        user.save()

@receiver(post_delete, sender = Admin)
def delete_admin(sender, instance, **kwargs):
    User.objects.filter(username = instance.MailId).delete()

class Applicant(models.Model):
    Id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    FirstName = models.CharField(max_length = 30, validators = [name_regex])
    LastName = models.CharField(max_length = 30, validators = [name_regex])
    UserName = models.CharField(max_length = 30, validators = [name_regex], unique = True)
    MailId = models.EmailField(unique = True)
    Password = models.CharField(max_length = 25, validators = [MinLengthValidator(8)])
    PhoneNo = models.CharField(validators=[phone_regex], max_length=10)

    def __str__(self):
        return self.UserName

    class Meta:
        ordering = ["UserName"]
    
@receiver(post_save, sender=Applicant)
def save_p_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.MailId, email=instance.MailId, password=instance.Password)
        user.profile.type = 'u'
    user.save()

@receiver(post_delete, sender=Applicant)
def delete_p_user(sender, instance, **kwargs):
    User.objects.filter(username=instance.MailId).delete()

class Application(models.Model):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    CITIES = (
        ('ben', 'Bangalore'),
        ('mys', 'Mysore'),
        ('hub', 'Hubballi'),
        ('mdy', 'Mandya')
    )

    STATES = (
       ( 'ap', 'Andhra Pradesh'),
       ( 'mh', 'Maharashtra'),
        ('ka', 'Karnataka'),
    )


    ApplicantId = models.OneToOneField('Applicant', blank = False, null = False, on_delete = models.CASCADE)
    FirstName = models.CharField(max_length = 30, validators = [name_regex], null = False, blank = False, default='sagar')
    MiddleName = models.CharField(max_length = 30, validators = [name_regex], default='sagar')
    LastName = models.CharField(max_length = 30, validators = [name_regex], default='sagar')
    DateOfBirth = models.DateField(default ='1997-09-01')
    Gender = models.CharField(max_length=10, choices = GENDER, default = 'm')
    FlatNo = models.CharField(max_length=15, default ='32')
    State = models.CharField(max_length = 30, choices = CITIES, default='a')
    City = models.CharField(max_length = 30, choices = STATES , default='a')
    PlaceOfBirth = models.CharField(max_length = 30, blank = False, null = False, default='somewhere')

class Documents(models.Model):
        ApplicationId= models.OneToOneField('Application', blank = False, null = True, on_delete = models.CASCADE)
        Photo = models.ImageField(upload_to = get_photo_folder, validators = [validate_file_extension, file_size_photo],  default = 'sagarstorm/a.jpg')
        AddressProof = models.ImageField(upload_to = get_address_folder, validators = [validate_file_extension, file_size])
        BirthCertificate = models.ImageField(upload_to = get_birth_certificate_folder, validators = [validate_file_extension, file_size])
        PaymentReceipt = models.ImageField(upload_to = get_payment_receipt_folder, validators = [validate_file_extension, file_size])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(default='u', max_length=1)

    def __str__(self):
        return self.user.username + " " + self.type

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Status(models.Model):
    ApplicationId = models.OneToOneField('Application', blank = False, null = True, on_delete = models.CASCADE)
    Message = models.CharField(max_length = 500, blank = False, null = False)



## add a regex validator for department id
# use either departmentid or mailId for police identification

class PoliceDepartment(models.Model):
    DepartmentId = models.CharField(max_length = 6, blank = False, null = False, validators = [MinLengthValidator(6)])
    DIVISION = (
        ('bn', 'Bangalore-North'),
        ('bs', 'Bangalore-South'),
        ('be', 'Bangalore-East'),
        ('bbmp', 'Bangalore-BBMP')
    )

    DISTRICT = (
        ('ben', 'Bangalore'),
        ('mys', 'Mysore'),
        ('hub', 'Hubballi'),
        ('mdy', 'Mandya')
    )

    STATES = (
       ( 'ap', 'Andhra Pradesh'),
       ( 'mh', 'Maharashtra'),
        ('ka', 'Karnataka'),
    )

    Division = models.CharField(max_length = 30, choices = DIVISION, default = 'bn')
    District = models.CharField(max_length = 30, choices = DISTRICT, default = 'ben')
    State = models.CharField(max_length = 30, choices = STATES, default = 'ka' )
    MailId = models.EmailField(unique = True)
    Password = models.CharField(max_length = 25, validators = [MinLengthValidator(8)])

@receiver(post_save, sender = PoliceDepartment)
def save_police_department(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.MailId, email=instance.MailId, password=instance.Password)
        user.profile.type = 'p'
        user.save()

@receiver(post_delete, sender = PoliceDepartment)
def delete_police_department(sender, instance, **kwargs):
    User.objects.filter(username = instance.MailId).delete()

